import sys
import socket
import logging
import threading
import queue
import time
from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, ICMP
from ipwhois import IPWhois

# Hide warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# A bucket to hold packets so the sniffer doesn't get stuck
packet_queue = queue.Queue()
stop_event = threading.Event()
ip_cache = {}

def get_org_name(ip_addr):
    """Lookup Organization with a short timeout."""
    if ip_addr in ip_cache:
        return ip_cache[ip_addr]
    
    if ip_addr.startswith("192.168.") or ip_addr.startswith("10."):
        return "Local Network"

    try:
        # We enforce a strict timeout here
        socket.setdefaulttimeout(2) 
        obj = IPWhois(ip_addr)
        results = obj.lookup_rdap(depth=1)
        
        # Try to find the Organization Name
        org = None
        objects = results.get('objects', {})
        for _, obj_data in objects.items():
            contact = obj_data.get('contact', {})
            if contact and 'name' in contact:
                org = contact['name']
                break

        if not org:
            org = results.get('asn_description', "Unknown Org")

        # Clean formatting
        org = " ".join(org.split())
        ip_cache[ip_addr] = org
        return org
    except Exception:
        ip_cache[ip_addr] = "Lookup Failed"
        return "Lookup Failed"

def packet_processor():
    """Background worker that prints packets."""
    while not stop_event.is_set():
        try:
            # Wait for a packet from the queue for up to 1 second
            packet_data = packet_queue.get(timeout=0.5)
            
            # Unpack data
            timestamp, proto, remote_ip, details = packet_data
            
            # Perform the slow lookup HERE (in the background)
            org_name = get_org_name(remote_ip)
            
            print(f"{timestamp:^10} | {proto:^5} | {remote_ip:<15} | {org_name:<30} | {details:<15}")
            packet_queue.task_done()
            
        except queue.Empty:
            continue
        except Exception as e:
            print(f"Error: {e}")

def packet_callback(packet):
    """
    Lightweight callback. 
    Just grabs data and puts it in the queue. 
    DOES NOT perform slow lookups.
    """
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        remote_ip = dst_ip if not dst_ip.startswith(("192.", "10.")) else src_ip
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        protocol = "Other"
        details = ""

        if TCP in packet:
            protocol = "TCP"
            details = f"Port: {packet[TCP].dport}"
        elif UDP in packet:
            protocol = "UDP"
            details = f"Port: {packet[UDP].dport}"
        elif ICMP in packet:
            protocol = "ICMP"
            details = "Ping"

        # Add to queue instead of printing directly
        packet_queue.put((timestamp, protocol, remote_ip, details))

def start_sniffer():
    print("="*90)
    print("                         THREADED PACKET SNIFFER WITH ORG LOOKUP                         ")
    print("="*90)
    print(f"{'TIME':^10} | {'PROTO':^5} | {'REMOTE IP':^15} | {'ORGANIZATION NAME':^30} | {'SERVICE':^15}")
    
    # 1. Start the background worker thread
    worker_thread = threading.Thread(target=packet_processor)
    worker_thread.daemon = True # Dies when main script dies
    worker_thread.start()

    try:
        # 2. Start Sniffing (Main Thread)
        sniff(prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("\n[*] Stopping Sniffer... (Waiting for queue to empty)")
        stop_event.set()
        # Give the worker a moment to finish
        time.sleep(1)
        sys.exit(0)

if __name__ == "__main__":
    start_sniffer()
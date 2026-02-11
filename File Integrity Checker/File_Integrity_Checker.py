import hashlib
import os
import json

def calculate_hash(filepath):
    """Calculates the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            # Read file in chunks to avoid memory issues with large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def update_baseline(directory, baseline_file="baseline.json"):
    """Creates a new baseline of file hashes."""
    baseline = {}
    print(f"\n[*] Calculating hashes for files in: {directory}")
    
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = calculate_hash(filepath)
            baseline[filepath] = file_hash
            print(f"    + {file} | Hash: {file_hash[:10]}...")
            
    with open(baseline_file, 'w') as f:
        json.dump(baseline, f, indent=4)
    print(f"\n[+] Baseline saved to {baseline_file}")

def check_integrity(baseline_file="baseline.json"):
    """Compares current files against the saved baseline."""
    try:
        with open(baseline_file, 'r') as f:
            baseline = json.load(f)
    except FileNotFoundError:
        print("[-] Baseline file not found. Please run update mode first.")
        return

    print("[*] Checking file integrity...")
    integrity_violated = False

    for filepath, stored_hash in baseline.items():
        current_hash = calculate_hash(filepath)
        
        if current_hash is None:
            print(f"⚠️  MISSING: {filepath} has been deleted!")
            integrity_violated = True
        elif current_hash != stored_hash:
            print(f"🚨 ALERT: {filepath} has been MODIFIED!")
            integrity_violated = True
        else:
            # Optional: Print OK for unchanged files
            # print(f"✅ OK: {filepath}")
            pass

    if not integrity_violated:
        print("\n[+] System Clean: No modifications detected.")

def main():
    print("--- File Integrity Checker ---")
    print("1. Create/Update Baseline")
    print("2. Check Integrity")
    
    choice = input("Select mode (1/2): ")
    
    # For default demo, we scan the current directory
    target_dir = "." 
    
    if choice == '1':
        print("\n--- Create/Update Baseline ---")
        print("a. Scan another directory")
        print("b. Scan current directory")
        decision = input("Enter your decision(a/b): ")
        if decision == 'a':
            target_dir = input("Enter the directory path you want to scan: ")
        if decision == 'b':
            pass
        else:
            print("Invalid selection. Defaulting to current directory.")
        
        update_baseline(target_dir)
    elif choice == '2':
        check_integrity()
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
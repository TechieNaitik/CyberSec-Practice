# CyberSec-Scripts

This repository contains a growing collection of **cybersecurity-related scripts** developed for learning, experimentation, and practical use.  
The focus is on networking, cryptography, password security, and reconnaissance utilities.

> ⚠️ **Disclaimer**  
> All tools in this repository are intended for **educational purposes and ethical use only**.  
> Do **not** use these scripts on systems or networks you do not own or have explicit permission to test.

---

## Repository Structure

```text
CyberSec-Practice
├── Caesar_Cipher.py
├── File Integrity Checker/
│   ├── Baseline.json
│   └── File_Integrity_Checker.py
├── Web Directory Enumerator/
│   ├── common_dir.txt
│   ├── Web_Dir_Enum.py
│   └── Dummy_Website/
├── Nmap_PortScanner.py
├── Password_Checker.py
├── Password_Generator.py
├── Password_Manager.py
├── Packet_Sniffer.py
├── WhoIs.py
├── .gitignore
└── README.md
```

## Scripts

### 🔐 Caesar_Cipher.py

A basic implementation of the **Caesar Cipher** encryption and decryption technique.  
Demonstrates fundamental cryptographic concepts such as substitution ciphers and key-based shifting.

---

### 🌐 Nmap_PortScanner.py

A Python-based port scanner that leverages **Nmap** to identify open ports and services on a target system.  
Useful for learning network reconnaissance and basic penetration testing workflows.

> Requires Nmap to be installed on the system.

---

### 🔑 Password_Checker.py

Checks password strength based on predefined rules such as:

- Length
- Character variety
- Common password patterns

Helps understand password security and validation mechanisms.

---

### 🔐 Password_Generator.py

Generates strong, random passwords using configurable parameters like:

- Length
- Character sets (uppercase, lowercase, numbers, symbols)

Useful for secure credential creation.

---

### 🗄️ Password_Manager.py

A simple password management utility to store and retrieve credentials securely.  
Designed as a learning project to explore secure storage concepts.

> ⚠️ Not intended for production use.

---

### 🌍 WhoIs.py

Performs **WHOIS lookups** to retrieve domain registration and ownership information.  
Introduces basic OSINT and reconnaissance techniques.

---

### 🛡️ File_Integrity_Checker.py

A security tool that calculates **SHA-256 hashes** of files to detect unauthorized modifications.  
Demonstrates the concept of **Data Integrity** and how hashing differs from encryption.

- **Mode 1:** Creates a baseline (snapshot) of file hashes.
- **Mode 2:** Compares current files against the baseline to detect tampering.

---

## 🕵️ Web_Dir_Enum.py

A reconnaissance tool that performs directory brute-forcing to discover hidden paths and sensitive files on a web server. Demonstrates how automated fuzzing can uncover "security through obscurity" vulnerabilities by identifying unlinked resources.

### Usage

- Navigate to the Dummy_Website directory in your terminal and start the local server:

```bash
cd 'Web Directory Enumerator'
cd Dummy_Website
python -m http.server 8000
```

- Open another terminal and run:

```bash
cd 'Web Directory Enumerator'
python Web_Dir_Enum.py 127.0.0.1:8000 common_dir.txt
```

> ⚠️ Warning: Usage of Web_Dir_Enum.py for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable laws.

---

## 🛡️ Packet_Sniffer.py

A beginner-friendly network packet sniffer using the **Scapy** library. This script captures live network traffic and displays key details such as IP addresses, ports, and protocols.

### Usage Guide

1. Install dependencies: You must install the **scapy** library before running this script.

    ```bash
    pip install scapy
    ```

2. Run the script: This script requires direct access to network interfaces, which usually requires Administrator (Windows) or Root (Linux/macOS) privileges.

   - Windows: Open Command Prompt or PowerShell as administrator. Run:

   ```bash
   python Packet_Sniffer.py
   ```

   - Linux/MacOS: Use sudo to run the script.

   ```bash
   sudo Packet_Sniffer.py
   ```

3. After executing the script:

   - Press Ctrl+C to stop the capture gracefully.

>⚠️ This tool is for educational purposes and network troubleshooting. Always ensure you have permission to monitor the network you are on.
---

## Technologies Used

- **Python 3.13**
- **Nmap**
- Python libraries (`os`, `random`, `string`, `math`, `re`, `socket`, `hashlib`, `getpass`, `json`, `python-nmap` `requests`, `sys`, `scapy`)

---

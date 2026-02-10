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
├── Nmap_PortScanner.py
├── Password_Checker.py
├── Password_Generator.py
├── Password_Manager.py
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

## Technologies Used

- **Python 3.13**
- **Nmap**
- Python libraries (`os`, `random`, `string`, `math`, `re`, `socket`, `hashlib`, `getpass`)

---

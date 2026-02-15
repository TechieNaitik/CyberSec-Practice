# CyberSec-Scripts

This repository contains a growing collection of **cybersecurity-related scripts** developed for learning, experimentation, and practical use.  
The focus is on networking, cryptography, password security, and reconnaissance utilities.

---

## Repository Structure

```text
CyberSec-Scripts
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
│
├── Cryptography/
│   ├──Caesar_Cipher.py
|   └── Steganography/
│       ├── Pic.jpg (Normal Image)
│       ├── secret.png (Encoded Image)
│       └── Steganography.py
|
├── Forensics/
│   └── Metadata Extractor/
│       ├── IMG_1971.jpeg
│       ├── IMG_1972.jpeg
│       └──  Metadata_Extractor.py
│
├── Network Tools/
│   ├── Nmap_PortScanner.py
│   ├── Packet_Sniffer.py
│   └── WhoIs.py
│
├── System Security/
│   ├── File Integrity Checker/
│   │   ├── baseline.json
│   │   └── File_Integrity_Checker.py
│   └── Keylogger/
│       ├── keylog.txt
│       └── Keylogger.py
│
├── Utilities/
│   ├── Password_Checker.py
│   ├── Password_Generator.py
│   └── Password_Manager.py
│
└── Web Security/
    ├── Hash Cracker/
    │   ├── Hash_Cracker.py
    │   └── passlist.txt
    │
    └── Web Directory Enumerator/
        ├── common_dir.txt
        ├── Dummy_Website/
        └── Web_Dir_Enum.py
```

## Scripts

### 🔐 Caesar_Cipher.py

A basic implementation of the **Caesar Cipher** encryption and decryption technique.  
Demonstrates fundamental cryptographic concepts such as substitution ciphers and key-based shifting.

**Usage:**

```powershell
cd Cryptography
python Caesar_Cipher.py
```

---

### 🖼️ Steganography.py

A **Least Significant Bit (LSB) Steganography** tool that hides secret messages inside images without visibly altering them.  
This script demonstrates how to conceal data within digital media by modifying the least significant bits of pixel values, making the changes imperceptible to the human eye.

**Features:**

- Encode text messages into images (PNG format recommended)
- Decode hidden messages from steganographic images
- Automatic delimiter detection for message extraction
- Image capacity validation to ensure message fits

> Requires the **Pillow (PIL)** library to be installed.

**Usage:**

1. Install dependencies:

   ```powershell
   pip install Pillow
   ```

2. Run the program:

   ```powershell
   cd Cryptography\Steganography
   python Steganography.py
   ```

3. Select an option:
   - **Option 1 (Encode)**: Hide a message in an image
     - Provide the path to your input image (e.g., `Pic.jpg`)
     - Enter the secret message you want to hide
     - Specify the output filename (will be saved as PNG to prevent compression loss)
   - **Option 2 (Decode)**: Reveal a hidden message
     - Provide the path to an encoded image (e.g., `secret.png`)
     - The hidden message will be extracted and displayed

---

### 🔍 Metadata_Extractor.py

A digital forensics tool that extracts **EXIF metadata** from image files.  
It retrieves detailed information such as camera settings, date/time, and GPS coordinates if available.

**Features:**

- Extract camera make and model
- Identify exposure settings (aperture, shutter speed, ISO)
- Extract GPS coordinates and generate a Google Maps link
- Support for common image formats (JPEG, PNG, etc.)

> Requires **exifread** and **Pillow** libraries.

**Usage:**

1. Install dependencies:

   ```powershell
   pip install exifread Pillow
   ```

2. Run the script:

   ```powershell
   cd "Forensics\Metadata Extractor"
   python Metadata_Extractor.py <path_to_image>
   ```

---

### 🌐 Nmap_PortScanner.py

A Python-based port scanner that leverages **Nmap** to identify open ports and services on a target system.  
Useful for learning network reconnaissance and basic penetration testing workflows.

> Requires Nmap to be installed on the system.

**Usage:**

```powershell
cd "Network Tools"
python Nmap_PortScanner.py
```

---

### 🛡️ Packet_Sniffer.py

A beginner-friendly network packet sniffer using the **Scapy** library. This script captures live network traffic and displays key details such as IP addresses, ports, and protocols.

**Usage:**

1. Install dependencies: You must install the **scapy** library before running this script.

   ```powershell
   pip install scapy
   ```

2. Run the script: This script requires direct access to network interfaces, which usually requires Administrator (Windows) or Root (Linux/macOS) privileges.
   - Windows: Open Command Prompt or PowerShell as administrator. Run:

   ```powershell
   cd "Network Tools"
   python Packet_Sniffer.py
   ```

   - Linux/MacOS: Use sudo to run the script.

   ```bash
   sudo python Packet_Sniffer.py
   ```

3. After executing the script:
   - Press Ctrl+C to stop the capture gracefully.

---

### 🌍 WhoIs.py

Performs **WHOIS lookups** to retrieve domain registration and ownership information.  
Introduces basic OSINT and reconnaissance techniques.

**Usage:**

```powershell
cd "Network Tools"
python WhoIs.py
```

---

### 🛡️ File_Integrity_Checker.py

A security tool that calculates **SHA-256 hashes** of files to detect unauthorized modifications.  
Demonstrates the concept of **Data Integrity** and how hashing differs from encryption.

- **Mode 1:** Creates a baseline (snapshot) of file hashes.
- **Mode 2:** Compares current files against the baseline to detect tampering.

**Usage:**

```powershell
cd "System Security\File Integrity Checker"
python File_Integrity_Checker.py
```

---

### ⌨️ Keylogger.py

A Python-based keylogger that listens for and records keyboard events into a local file.  
Demonstrates how input listeners work and the importance of system security against unauthorized monitoring.

**Features:**

- Captures alphanumeric and special keys
- Logs keystrokes to `keylog.txt`
- Runs as a background listener
- Safe exit using the `Esc` key

> Requires the **pynput** library to be installed.

**Usage:**

1. Install dependencies:

   ```powershell
   pip install pynput
   ```

2. Run the program:

   ```powershell
   cd "System Security\Keylogger"
   python Keylogger.py
   ```

---

### 🔑 Password_Checker.py

Checks password strength based on predefined rules such as:

- Length
- Character variety
- Common password patterns

Helps understand password security and validation mechanisms.

**Usage:**

```powershell
cd Utilities
python Password_Checker.py
```

---

### 🔐 Password_Generator.py

Generates strong, random passwords using configurable parameters like:

- Length
- Character sets (uppercase, lowercase, numbers, symbols)

Useful for secure credential creation.

**Usage:**

```powershell
cd Utilities
python Password_Generator.py
```

---

### 🗄️ Password_Manager.py

A simple password management utility to store and retrieve credentials securely.  
Designed as a learning project to explore secure storage concepts.

**Usage:**

```powershell
cd Utilities
python Password_Manager.py
```

---

### 🔓 Hash_Cracker.py

A simulation tool for performing dictionary attacks against hashed passwords (MD5, SHA1, SHA256). Demonstrates how weak passwords can be reversed using pre-computed wordlists and highlights the difference between one-way hashing and reversible encryption.

**Usage:**

1. Run the program using the command:

   ```powershell
   cd "Web Security\Hash Cracker"
   python Hash_Cracker.py
   ```

2. Enter a hash you want to crack.

3. Enter the hash type (MD5, SHA1 or SHA256).

4. Enter the path of the passlist file (.txt) to check against possible passwords.

---

### 🕵️ Web_Dir_Enum.py

A reconnaissance tool that performs directory brute-forcing to discover hidden paths and sensitive files on a web server. Demonstrates how automated fuzzing can uncover "security through obscurity" vulnerabilities by identifying unlinked resources.

**Usage:**

- Navigate to the Dummy_Website directory in your terminal and start the local server:

```powershell
cd "Web Security\Web Directory Enumerator\Dummy_Website"
python -m http.server 8000
```

- Open another terminal and run:

```powershell
cd "Web Security\Web Directory Enumerator"
python Web_Dir_Enum.py 127.0.0.1:8000 common_dir.txt
```

---

## Technologies Used

- **Python 3.13**
- **Nmap**
- Python libraries (`os`, `random`, `string`, `math`, `re`, `socket`, `hashlib`, `getpass`, `json`, `python-nmap`, `requests`, `sys`, `scapy`, `pillow`, `exifread`, `pynput`, `ipwhois`)

---

## ⚠️ Legal & Ethical Disclaimer

**All tools and scripts in this repository are intended for educational purposes and ethical use only.**

### Important Guidelines

- ✅ **DO** use these tools on systems and networks you **own** or have **explicit written permission** to test
- ✅ **DO** use these tools for learning, security research, and authorized penetration testing
- ✅ **DO** follow responsible disclosure practices if you discover vulnerabilities
- ❌ **DO NOT** use these tools to attack, compromise, or access unauthorized systems
- ❌ **DO NOT** use these tools for illegal activities or malicious purposes
- ❌ **DO NOT** assume implied consent — always obtain explicit authorization

### Specific Tool Warnings

- **Password Manager**: Not intended for production use. Use established password management solutions for actual credential storage.
- **Web Directory Enumerator**: Usage for attacking targets without prior mutual consent is **illegal**. It is the end user's responsibility to obey all applicable laws.
- **Packet Sniffer**: Always ensure you have permission to monitor the network you are on. Unauthorized network monitoring may violate privacy laws and regulations.
- **Hash Cracker**: Do not use against unauthorized targets. Cracking passwords without authorization is illegal in most jurisdictions.

### Legal Responsibility

By using any script from this repository, you acknowledge that:

- You are solely responsible for your actions
- The repository maintainer is not liable for any misuse or damage caused by these tools
- Unauthorized access to computer systems is illegal under laws such as the Computer Fraud and Abuse Act (CFAA) in the United States and similar legislation worldwide

**Use responsibly. Stay ethical. Stay legal.**

---

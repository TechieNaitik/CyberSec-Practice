import requests
import sys

def enumerate_directories(target_url, wordlist_file):
    # Ensure URL ends with a slash
    if not target_url.endswith("/"):
        target_url += "/"

    print(f"[*] Starting directory enumeration on: {target_url}")
    print(f"[*] Using wordlist: {wordlist_file}")
    print("-" * 40)

    try:
        with open(wordlist_file, 'r') as file:
            for line in file:
                directory = line.strip()

                # --- THE FIX IS HERE ---
                # Skip empty lines OR lines that start with '#'
                if not directory or directory.startswith("#"):
                    continue
                # -----------------------

                full_url = f"{target_url}{directory}"

                try:
                    response = requests.get(full_url, timeout=3)
                    
                    if response.status_code == 200:
                        print(f"[+] FOUND (200): {full_url}")
                    elif response.status_code == 403:
                        print(f"[!] FORBIDDEN (403): {full_url}")
                    elif response.status_code == 301:
                        print(f"[>] REDIRECT (301): {full_url}")

                except requests.exceptions.ConnectionError:
                    pass
                except KeyboardInterrupt:
                    print("\n[!] Scan interrupted by user.")
                    sys.exit()

    except FileNotFoundError:
        print(f"[-] Error: Wordlist file '{wordlist_file}' not found.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

    print("-" * 40)
    print("[*] Scan complete.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Web_Dir_Enum.py <TARGET_URL> <WORDLIST_FILE>")
    else:
        target = sys.argv[1]
        wordlist = sys.argv[2]
        enumerate_directories(target, wordlist)
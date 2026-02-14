import hashlib
import time
import os

# ==========================================
# SECURITY DISCLAIMER
# ==========================================
# This script is for EDUCATIONAL and ETHICAL use only.
# It is designed to demonstrate how dictionary attacks work logic-wise
# and to highlight the importance of strong password policies.
# Do not use this against unauthorized targets.
# ==========================================

def get_hash_object(algorithm, password):
    """
    Returns the hash object based on the selected algorithm.
    """
    encoded_password = password.encode('utf-8')
    
    if algorithm == 'md5':
        return hashlib.md5(encoded_password)
    elif algorithm == 'sha1':
        return hashlib.sha1(encoded_password)
    elif algorithm == 'sha256':
        return hashlib.sha256(encoded_password)
    else:
        return None

def main():
    print("-------------------------------------------------")
    print("      EDUCATIONAL PASSWORD HASH CRACKER         ")
    print("-------------------------------------------------")
    
    # --- EDUCATIONAL NOTES ---
    # 1. Hashing vs. Encryption:
    #    - Encryption is two-way: Data is scrambled and can be unscrambled with a key.
    #    - Hashing is one-way: Data is turned into a unique string of characters (digest).
    #      You cannot mathematically reverse a hash to get the original password.
    #
    # 2. Dictionary Attack:
    #    - Since we cannot reverse the hash, we guess.
    #    - We take a list of common words (dictionary), hash them one by one,
    #      and compare the result to the stolen hash. If they match, we found the password.
    # -------------------------

    # 1. User Inputs
    target_hash = input("[?] Enter the target hash to crack: ").strip().lower()
    
    if not target_hash:
        print("[-] Error: Hash cannot be empty.")
        return

    print("\nSelect Hash Algorithm:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    
    choice = input("[?] Enter selection (1-3): ").strip()
    
    algorithm_map = {'1': 'md5', '2': 'sha1', '3': 'sha256'}
    selected_alg = algorithm_map.get(choice)

    if not selected_alg:
        print("[-] Error: Invalid algorithm selection.")
        return

    wordlist_path = input("[?] Enter path to dictionary file (e.g., passlist.txt): ").strip()

    # 2. Validate File Existence
    if not os.path.exists(wordlist_path):
        print(f"[-] Error: File '{wordlist_path}' not found.")
        return

    print(f"\n[+] Starting {selected_alg.upper()} dictionary attack...")
    print(f"[+] Target: {target_hash}")
    
    start_time = time.time()
    password_found = False
    
    # 3. The Attack Loop
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                word = line.strip()
                
                # Skip empty lines
                if not word:
                    continue
                
                # Hash the current word from the dictionary
                hash_obj = get_hash_object(selected_alg, word)
                digest = hash_obj.hexdigest()
                
                # Compare the generated hash with the target hash
                if digest == target_hash:
                    password_found = True
                    end_time = time.time()
                    time_taken = end_time - start_time
                    
                    print("\n" + "="*40)
                    print("SUCCESS! Password Cracked.")
                    print("="*40)
                    print(f"[+] Password:    {word}")
                    print(f"[+] Time Taken:  {time_taken:.4f} seconds")
                    break
        
        if not password_found:
            print("\n[-] Failed: Password not found in the provided dictionary.")
            print("[-] Tip: The password might be too complex or not in the list.")

    except Exception as e:
        print(f"\n[-] An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
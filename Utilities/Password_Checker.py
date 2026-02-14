import math
import re

def calculate_entropy(password):
    """
    Calculates the entropy (bits) based on the character pool size.
    Formula: Entropy = Length * log2(Pool Size)
    """
    pool_size = 0
    
    # Check for different character sets using Regex
    if re.search(r'[a-z]', password):
        pool_size += 26  # Lowercase
    if re.search(r'[A-Z]', password):
        pool_size += 26  # Uppercase
    if re.search(r'\d', password):
        pool_size += 10  # Digits
    if re.search(r'[^a-zA-Z\d]', password):
        pool_size += 32  # Approximate count of special characters (symbols)

    # Prevent math error if empty
    if pool_size == 0:
        return 0
        
    # Calculate Entropy
    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)

def rate_password(password):
    # 1. Calculate Entropy
    entropy = calculate_entropy(password)
    
    # 2. Determine Strength based on bits of entropy
    # < 28 bits: Very Weak (Instant crack)
    # 28 - 35 bits: Weak
    # 36 - 59 bits: Medium (Reasonable for low-risk accounts)
    # 60+ bits: Strong (Hard to brute force)
    
    rating = ""
    if entropy < 28:
        rating = "Weak 🔴"
    elif entropy < 60:
        rating = "Medium 🟡"
    else:
        rating = "Strong 🟢"
        
    return f"Password: {password}\nEntropy: {entropy} bits\nRating: {rating}"

# --- Test the Tool ---
print("--- Password Strength Checker ---")
user_input = input("Enter a password to test: ")
print("-" * 30)
print(rate_password(user_input))
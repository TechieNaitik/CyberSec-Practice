from PIL import Image
import os

def string_to_binary(message):
    """Convert a string to its binary representation."""
    return ''.join(format(ord(char), '08b') for char in message)

def binary_to_string(binary_data):
    """Convert a binary string back to text."""
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_chars = []
    for byte in all_bytes:
        decoded_chars.append(chr(int(byte, 2)))
    return ''.join(decoded_chars)

def encode_message(image_path, secret_message, output_path):
    """Encodes a secret message into the LSB of an image."""
    try:
        image = Image.open(image_path)
        # Convert image to RGB to ensure 3 channels per pixel
        image = image.convert("RGB")
        pixels = list(image.getdata())
        
        # Add a delimiter to identify the end of the message
        delimiter = "#####"
        full_message = secret_message + delimiter
        binary_message = string_to_binary(full_message)
        
        # Check if the image is large enough to hold the message
        # Each pixel has 3 values (R, G, B), so we can store 3 bits per pixel.
        max_capacity = len(pixels) * 3
        if len(binary_message) > max_capacity:
            raise ValueError(f"Message is too long for this image! Image capacity: {max_capacity} bits. Message size: {len(binary_message)} bits.")
        
        encoded_pixels = []
        data_index = 0
        message_len = len(binary_message)

        for pixel in pixels:
            if data_index < message_len:
                r, g, b = pixel
                
                # Encode bit into Red LSB
                if data_index < message_len:
                    # Clear the LSB (make it 0) using bitwise AND with inverted 1
                    # Then use bitwise OR to set it to the message bit
                    r = (r & ~1) | int(binary_message[data_index])
                    data_index += 1
                
                # Encode bit into Green LSB
                if data_index < message_len:
                    g = (g & ~1) | int(binary_message[data_index])
                    data_index += 1
                
                # Encode bit into Blue LSB
                if data_index < message_len:
                    b = (b & ~1) | int(binary_message[data_index])
                    data_index += 1
                
                encoded_pixels.append((r, g, b))
            else:
                # If message is finished, just append the rest of the original pixels
                encoded_pixels.append(pixel)

        # Create a new image with the modified pixels
        encoded_image = Image.new(image.mode, image.size)
        encoded_image.putdata(encoded_pixels)
        
        # Force PNG output to prevent compression artifacts destroying LSB data
        if not output_path.lower().endswith(".png"):
            output_path = os.path.splitext(output_path)[0] + ".png"
            print("Note: Output extension changed to .png to prevent data loss via compression.")
            
        encoded_image.save(output_path)
        print(f"Success! Encoded image saved as {output_path}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def decode_message(image_path):
    """Decodes a secret message from the LSB of an image."""
    try:
        image = Image.open(image_path)
        image = image.convert("RGB")
        pixels = list(image.getdata())
        
        binary_data = ""
        delimiter = "#####"
        
        for pixel in pixels:
            r, g, b = pixel
            
            # Extract LSB from Red, Green, and Blue channels
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

        # Process the binary data in chunks of 8 bits (1 byte)
        all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
        
        decoded_message = ""
        for byte in all_bytes:
            # Convert byte to character
            char = chr(int(byte, 2))
            decoded_message += char
            
            # Check if the message ends with the delimiter
            if decoded_message.endswith(delimiter):
                # Return message without the delimiter
                return decoded_message[:-len(delimiter)]
                
        # If we reach here, no delimiter was found
        return "No hidden message found (or delimiter missing)."

    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("=== LSB Steganography Tool ===")
    while True:
        print("\nMenu:")
        print("1. Encode (Hide Message)")
        print("2. Decode (Reveal Message)")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            img_path = input("Enter input image path (e.g., input.jpg): ")
            msg = input("Enter secret message: ")
            out_path = input("Enter output filename (e.g., secret.png): ")
            encode_message(img_path, msg, out_path)
            
        elif choice == '2':
            img_path = input("Enter encoded image path: ")
            print("Decoding...")
            result = decode_message(img_path)
            print(f"Hidden Message: {result}")
            
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
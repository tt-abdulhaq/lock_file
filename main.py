#!/usr/bin/env python3
"""
Encryptor CLI Tool
A cross-platform encryption and decryption tool for files using a password-based key.
Works on both Windows & Linux as a standalone CLI tool.
"""

from cryptography.fernet import Fernet, InvalidToken
import argparse
import hashlib
import base64
import os
import sys

# Convert a string to a 32-byte key
def convert_string_to_key(key_string):
    if not key_string:
        raise ValueError("Encryption key cannot be empty.")
    return base64.urlsafe_b64encode(hashlib.sha256(key_string.encode()).digest())

# Encrypt a file
def encrypt_file(input_file, key):
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Error: File '{input_file}' not found.")
        
        output_file = f"{input_file}.encrypted"
        fernet = Fernet(key)

        with open(input_file, "rb") as file:
            file_data = file.read()
        
        encrypted_data = fernet.encrypt(file_data)

        with open(output_file, "wb") as file:
            file.write(encrypted_data)
        os.remove(input_file)

        print(f"✅ File '{input_file}' encrypted successfully as '{output_file}'")
    
    except FileNotFoundError as e:
        print(f"❌ {e}")
    except PermissionError:
        print(f"❌ Permission denied. Check your file permissions.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Decrypt a file
def decrypt_file(input_file, key):
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Error: File '{input_file}' not found.")

        if not input_file.endswith(".encrypted"):
            raise ValueError("Invalid file format. Expected a '.encrypted' file.")

        output_file = input_file.replace(".encrypted", "")
        fernet = Fernet(key)

        with open(input_file, "rb") as file:
            encrypted_data = file.read()
        
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(output_file, "wb") as file:
            file.write(decrypted_data)
        os.remove(input_file)

        print(f"✅ File '{input_file}' decrypted successfully as '{output_file}'")

    except InvalidToken:
        print("❌ Decryption failed. Incorrect key or corrupted file.")
    except FileNotFoundError as e:
        print(f"❌ {e}")
    except ValueError as e:
        print(f"❌ {e}")
    except PermissionError:
        print(f"❌ Permission denied. Check your file permissions.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Command-line argument handling
def main():
    parser = argparse.ArgumentParser(
        description="🔐 Encryptor - A CLI Tool for File Encryption and Decryption"
    )
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Choose mode: encrypt or decrypt")
    parser.add_argument("--input", required=True, help="File to encrypt/decrypt")
    parser.add_argument("--key", required=True, help="Secret key (string) for encryption/decryption")

    args = parser.parse_args()

    try:
        key = convert_string_to_key(args.key)

        if args.mode == "encrypt":
            encrypt_file(args.input, key)
        elif args.mode == "decrypt":
            decrypt_file(args.input, key)
    
    except ValueError as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()

from Crypto.Cipher import AES
import os

# Function to encrypt a file
def encrypt_file(filename, key):
    cipher = AES.new(key, AES.MODE_EAX)  # AES encryption in EAX mode
    with open(filename, 'rb') as file:
        plaintext = file.read()
    
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    with open(filename + ".encrypted", 'wb') as file:
        file.write(cipher.nonce)  # Save the nonce
        file.write(tag)  # Save the tag
        file.write(ciphertext)  # Save the ciphertext

# Function to decrypt a file
def decrypt_file(filename, key):
    with open(filename, 'rb') as file:
        nonce = file.read(16)  # First 16 bytes is the nonce
        tag = file.read(16)  # Next 16 bytes is the tag
        ciphertext = file.read()  # The rest is the encrypted data
    
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
    
    with open(filename[:-10], 'wb') as file:  # Remove ".encrypted" from filename
        file.write(decrypted_data)

if _name_ == "_main_":
    # AES key (16 bytes for AES-128)
    key = b'Sixteen byte key'  # Fixed key for simplicity (16 bytes)

    # Ask the user to input the filename
    filename = input("Enter the name of the file to encrypt (e.g., 'sample.txt'): ")

    # Check if the file exists before proceeding
    if not os.path.exists(filename):
        print(f"The file '{filename}' does not exist.")
    else:
        # Encrypt the file
        encrypt_file(filename, key)
        print(f"File '{filename}' encrypted successfully!")

        # Decrypt the file
        encrypted_filename = filename + ".encrypted"
        decrypt_file(encrypted_filename, key)
        print(f"File '{encrypted_filename}' decrypted successfully!")

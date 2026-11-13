from cryptography.fernet import Fernet

# Load the secret key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Read the file to encrypt
with open("sample.txt", "rb") as file:
    original_data = file.read()

# Encrypt the data
encrypted_data = fernet.encrypt(original_data)

# Save encrypted data
with open("sample_encrypted.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

print("File encrypted successfully!")
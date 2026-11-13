import hashlib
from cryptography.fernet import Fernet

logged_in = False


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    hashed_password = hash_password(password)

    with open("users.txt", "a") as file:
        file.write(f"{username},{hashed_password}\n")

    print("Registration Successful!")


def login():
    global logged_in

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    hashed_password = hash_password(password)

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()

        for user in users:
            stored_username, stored_password = user.strip().split(",")

            if username == stored_username and hashed_password == stored_password:
                print("Login Successful!")
                logged_in = True
                return

        print("Invalid Username or Password!")

    except FileNotFoundError:
        print("No users found. Please register first.")


def encrypt_file():
    if not logged_in:
        print("Access Denied! Please Login First.")
        return

    with open("secret.key", "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)

    with open("sample.txt", "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open("sample_encrypted.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print("File encrypted successfully!")


def decrypt_file():
    if not logged_in:
        print("Access Denied! Please Login First.")
        return

    with open("secret.key", "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)

    with open("sample_encrypted.txt", "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open("decrypted_sample.txt", "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print("File decrypted successfully!")


while True:
    print("\n===== Secure File Encryption System =====")
    print("1. Register")
    print("2. Login")
    print("3. Encrypt File")
    print("4. Decrypt File")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        encrypt_file()

    elif choice == "4":
        decrypt_file()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")
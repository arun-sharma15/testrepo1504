import json
import re
import random
import string

# Caesar cipher encryption and decryption functions (pre-implemented)
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Password strength checker function (optional)
def is_strong_password(password):
    """
    Checks if the password is strong.1
    A strong password includes at least one uppercase letter, one lowercase letter,
    one digit, one special character, and is at least 8 characters long.
    """
    if (len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in string.punctuation for char in password)):
        return True
    return False

# Password generator function (optional)
def generate_password(length):
    """
    Generate a random strong password of the specified length.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    # Ensure the generated password is strong (optional safeguard)
    while not is_strong_password(password):
        password = ''.join(random.choice(all_chars) for _ in range(length))
        
    return password

# Initialize empty lists to store encrypted passwords, websites, and usernames
encrypted_passwords = []
websites = []
usernames = []

# Function to add a new password 
def add_password():
    """
    Add a new password to the password manager.
    Prompts the user for the website, username, and password, and stores them.
    Optionally, generates a random strong password if requested by the user.
    """
    website = input("Enter the website name: ")
    username = input("Enter the username: ")
    
    choice = input("Do you want to generate a random strong password? (yes/no): ").strip().lower()
    if choice == 'yes':
        while True:
            try:
                length = int(input("Enter the desired password length (minimum 8): "))
                if length < 8:
                    raise ValueError("Password length must be at least 8 characters.")
                break
            except ValueError as e:
                print(e)
        password = generate_password(length)
        print(f"Generated password: {password}")
    else:
        password = input("Enter the password: ")
        if not is_strong_password(password):
            print("Warning: The entered password is weak.")

    
    shift = random.randint(1, 25)  # Random shift for encryption
    encrypted_password = caesar_encrypt(password, shift)
    
    websites.append(website)
    usernames.append(username)
    # Store both the encrypted password and the shift as a tuple
    encrypted_passwords.append((encrypted_password, shift))
    print(f"Password for {website} added successfully!")

# Function to retrieve a password 
def get_password():
    """
    Retrieve a password for a given website.
    Prompts the user for the website name and displays the username and decrypted password.
    """
    website = input("Enter the website name: ")
    
    if website in websites:
        index = websites.index(website)
        username = usernames[index]
        encrypted_password, shift = encrypted_passwords[index]
        decrypted_password = caesar_decrypt(encrypted_password, shift)
        
        print(f"Username: {username}")
        print(f"Password: {decrypted_password}")
    else:
        print("Website not found in the password vault.")

# Function to save passwords to a JSON file
def save_passwords():
    """
    Save the password vault to a JSON file.
    This function saves passwords, websites, and usernames to a file named "vault.txt".
    """
    data = {
        "websites": websites,
        "usernames": usernames,
        "encrypted_passwords": encrypted_passwords
    }
    with open("vault.txt", "w") as file:
        json.dump(data, file)
    print("Passwords saved successfully!")

# Function to load passwords from a JSON file 
def load_passwords():
    """
    Load passwords from a JSON file into the password vault.
    This function populates the websites, usernames, and encrypted passwords lists.
    """
    global websites, usernames, encrypted_passwords
    try:
        with open("vault.txt", "r") as file:
            data = json.load(file)
            websites = data["websites"]
            usernames = data["usernames"]
            encrypted_passwords = data["encrypted_passwords"]
        print("Passwords loaded successfully!")
    except FileNotFoundError:
        print("vault.txt not found. Starting with an empty password vault.")
    except json.JSONDecodeError:
        print("Error loading passwords. The file may be corrupted.")
        
# Main method
def main():
    """
    Main function to implement the user interface for the password manager.
    """
    load_passwords()  # Load passwords at the start of the program
    print("Welcome to the Password Manager!")
    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Save Passwords")
        print("4. Load Passwords")
        print("5. Quit")
    
        choice = input("Enter your choice: ")
        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            save_passwords()
        elif choice == "4":
            load_passwords()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Execute the main function when the program is run
if __name__ == "__main__":
    main()

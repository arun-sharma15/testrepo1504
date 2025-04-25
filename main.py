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
    # ...

# Password generator function (optional)
def generate_password(length):
     """
    Generate a random strong password of the specified length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: A random strong password.
    """

# Initialize empty lists to store encrypted passwords, websites, and usernames
encrypted_passwords = []
websites = []
usernames = []

# Function to add a new password 
def add_password():
    print("Password is ready")
    """
    Add a new password to the password manager.

    This function should prompt the user for the website, username,  and password and store them to lits with same index. Optionally, it should check password strengh with the function is_strong_password. It may also include an option for the user to
    generate a random strong password by calling the generate_password function.

    Returns:
        None
    """

# Function to retrieve a password 
def get_password():
    """
    Retrieve a password for a given website.

    This function should prompt the user for the website name and
    then display the username and decrypted password for that website.

    Returns:
        None
    """

# Function to save passwords to a JSON file 
def save_passwords():
 """
    Save the password vault to a file.

    This function should save passwords, websites, and usernames to a text
    file named "vault.txt" in a structured format.

    Returns:
        None
    """
    # Combine the data into a list of dictionaries
    password_data = [
        {"website": website, "username": username, "password": password}
        for website, username, password in zip(websites, usernames, encrypted_passwords)
    ]

    # Save the data to a file
    with open("vault.txt", "w") as file:
        json.dump(password_data, file, indent=4)

    print("Passwords saved successfully!")


    Returns:
        None
    """
# Function to load passwords from a JSON file 
    Load passwords from a file into the password vault.

    This function should load passwords, websites, and usernames from a text
    file named "vault.txt" (or a more generic name) and populate the respective lists.

    Returns:
        None
    """
    
def load_passwords():
    global websites, usernames, encrypted_passwords

    try:
        # Open the file and load the data
        with open("vault.txt", "r") as file:
            password_data = json.load(file)

        # Clear existing lists and populate them with loaded data
        websites = [entry["website"] for entry in password_data]
        usernames = [entry["username"] for entry in password_data]
        encrypted_passwords = [entry["password"] for entry in password_data]

        print("Passwords loaded successfully!")

    except FileNotFoundError:
        print("No saved passwords found. Please save passwords first.")
    except json.JSONDecodeError:
        print("Error: The file is not in the correct format.")


  # Main method
def main():
# implement user interface 

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
        passwords = load_passwords()
        print("Passwords loaded successfully!")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

# Execute the main function when the program is run
if __name__ == "__main__":
    main()

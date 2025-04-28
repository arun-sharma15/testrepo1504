def get_password():
    """
    Retrieve a password for a given website.

    This function prompts the user for the website name and
    then displays the username and decrypted password for that website.

    Returns:
        None
    """
    website = input("Enter the website name: ")
    
    if website in websites:
        index = websites.index(website)
        username = usernames[index]
        encrypted_password = encrypted_passwords[index]
        
        # Decrypted password output
        shift = 3  # Shift value used for encryption (e.g., 3)
        decrypted_password = caesar_decrypt(encrypted_password, shift)
        
        print(f"Website: {website}")
        print(f"Username: {username}")
        print(f"Password: {decrypted_password}")
    else:
        print("No password found for the given website.")
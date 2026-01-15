import random
import string

def generate_password():
    print("--- Custom Password Generator ---")
    
    # Get password length from user
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Error: Length must be a positive number.")
            return
    except ValueError:
        print("Error: Please enter a valid number for the length.")
        return

    # Ask user for character type preferences
    include_upper = input("Include Uppercase letters? (Yes/No): ").strip().lower() == 'yes'
    include_lower = input("Include Lowercase letters? (Yes/No): ").strip().lower() == 'yes'
    include_numbers = input("Include Numbers? (Yes/No): ").strip().lower() == 'yes'
    include_special = input("Include Special characters? (Yes/No): ").strip().lower() == 'yes'

    # Build the character pool based on user choices
    char_pool = ""
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_numbers:
        char_pool += string.digits
    if include_special:
        char_pool += string.punctuation

    # Check if at least one character type was selected
    if not char_pool:
        print("Error: You must choose at least one character type!")
        return

    # Generate the random password
    password = ""
    for _ in range(length):
        password += random.choice(char_pool)

    # Display the result
    print("\nGenerated Password:")
    print(password)
    print("----------------------------")

if __name__ == "__main__":
    generate_password()

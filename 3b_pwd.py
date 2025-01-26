import random
import string

# Ask the user for the length of the password
length = int(input("Enter the desired password length: "))

# Ask the user if they want to include different types of characters
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

# Create an empty string to hold the possible characters
characters = ''

# Add characters based on user choices
if use_uppercase:
    characters += string.ascii_uppercase
if use_lowercase:
    characters += string.ascii_lowercase
if use_digits:
    characters += string.digits
if use_special_chars:
    characters += string.punctuation

# Initialize the password string
password = ''

# Generate the password using a for loop with an explicit index
for i in range(length):
    password += random.choice(characters)

# Output the generated password
print("Generated Password:", password)

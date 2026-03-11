import random
import string

def generate_password(length=12):
    # Define the characters we want to use
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters and join them together
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Generate and print a 16-character password
new_password = generate_password(16)
print(f"Your secure password is: {new_password}")
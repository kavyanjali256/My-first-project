
import random
import string

def generate_password(length=16):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    # Character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    # Ensure at least one character from each category
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest with a mix of all
    all_chars = upper + lower + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to remove patterns
    random.shuffle(password)

    return "".join(password)

# Example:
print("Generated Password:", generate_password(16))
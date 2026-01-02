import random
import string

def generate_password(length=16):
    if length < 2:
        raise ValueError("Password length must be at least 4.")

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = upper + lower + digits + symbols
    password += random.choices(all_chars, k=length - 2)

    random.shuffle(password)

    return "".join(password)

# --- User Interaction Loop ---
while True:
    try:
        length = int(input("Enter password length (minimum 2): "))
        pwd = generate_password(length)
        print("Generated Password:", pwd)
    except ValueError as e:
        print("Error:", e)
        continue

    again = input("Generate another? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Goodbye!")
        break

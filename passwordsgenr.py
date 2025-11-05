import random
import string

def generate_password():
    # Character sets
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Fill remaining characters randomly from all sets
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = [random.choice(all_chars) for _ in range(4)]

    # Combine all characters
    password_list = [upper, lower, digit, special] + remaining

    # Shuffle to randomize order
    random.shuffle(password_list)

    # Join as a string
    password = ''.join(password_list)
    return password

print("Generated Password:", generate_password())


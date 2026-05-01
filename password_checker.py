import re
import math

# Load common passwords
def load_common_passwords():
    try:
        with open("common_passwords.txt", "r") as f:
            return set(line.strip() for line in f)
    except:
        return set()

common_passwords = load_common_passwords()

def calculate_entropy(password):
    pool = 0
    if re.search("[a-z]", password): pool += 26
    if re.search("[A-Z]", password): pool += 26
    if re.search("[0-9]", password): pool += 10
    if re.search("[@#$%^&+=!]", password): pool += 10

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)

def check_patterns(password):
    patterns = ["123", "abc", "qwerty", "password"]
    for p in patterns:
        if p in password.lower():
            return True
    return False

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[@#$%^&+=!]", password):
        score += 1

    if password in common_passwords:
        return "Very Weak ❌ (Common Password)"

    if check_patterns(password):
        score -= 1

    entropy = calculate_entropy(password)

    if score <= 2:
        strength = "Weak ❌"
    elif score <= 4:
        strength = "Medium ⚠️"
    else:
        strength = "Strong ✅"

    return strength, entropy


# Run program
password = input("Enter password: ")
result = check_password_strength(password)

if isinstance(result, tuple):
    strength, entropy = result
    print(f"Strength: {strength}")
    print(f"Entropy: {entropy} bits")
else:
    print(result)

import time
import itertools
import string

# Target password (demo only)
target_password = "admin123"

# Load wordlist
def load_wordlist():
    try:
        with open("common_passwords.txt", "r") as f:
            return [line.strip() for line in f]
    except:
        return []

# WORDLIST ATTACK
def wordlist_attack(target):
    print("\n[+] Starting Wordlist Attack...")
    wordlist = load_wordlist()

    for word in wordlist:
        print("Trying:", word)
        time.sleep(0.1)

        if word == target:
            print("\n[✓] Password found using wordlist:", word)
            return True

    print("[!] Wordlist attack failed.")
    return False


# BRUTE FORCE (LIMITED LENGTH)
def brute_force_attack(target, max_length=4):
    print("\n[+] Starting Brute Force Attack...")
    chars = string.ascii_lowercase + string.digits

    start_time = time.time()

    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            guess = ''.join(attempt)
            print("Trying:", guess)

            if guess == target:
                end_time = time.time()
                print("\n[✓] Password found:", guess)
                print(f"Time taken: {round(end_time - start_time, 2)} seconds")
                return True

    print("[!] Brute force failed (limit reached).")
    return False


# MAIN EXECUTION
print("=== Password Attack Simulator ===")

if not wordlist_attack(target_password):
    brute_force_attack(target_password)

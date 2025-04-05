from itertools import product
import string

def brute_force(target_password):
    chars = string.ascii_lowercase
    for attempt in product(chars, repeat=len(target_password)):
        attempt_password = ''.join(attempt)
        print(f"Trying: {attempt_password}")
        if attempt_password == target_password:
            print(f"[+] Password found: {attempt_password}")
            return True
    return False

# Example usage
if __name__ == "__main__":
    brute_force("abc")

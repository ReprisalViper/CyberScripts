import hashlib

def crack_hash(hash_to_crack, wordlist):
    for word in wordlist:
        if hashlib.md5(word.encode()).hexdigest() == hash_to_crack:
            print(f"[+] Match found: {word}")
            return word
    print("[-] No match found.")
    return None

# Example usage
if __name__ == "__main__":
    hash_value = hashlib.md5("password".encode()).hexdigest()
    crack_hash(hash_value, ["1234", "password", "admin"])

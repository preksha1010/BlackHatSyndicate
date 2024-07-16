import hashlib
import itertools
import string
import time

# Hash to crack (MD5 hash of the password 'password')
hash_to_crack = '5f4dcc3b5aa765d61d8327deb882cf99'

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def brute_force_attack(hash_to_crack, max_length=4):
    characters = string.ascii_lowercase + string.digits  # Adjust the character set as needed
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            if md5_hash(guess) == hash_to_crack:
                return guess
    return None

def dictionary_attack(hash_to_crack, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for line in file:
            password = line.strip()
            if md5_hash(password) == hash_to_crack:
                return password
    return None

if __name__ == "__main__":
    # Demonstrate Brute Force Attack
    print("Starting brute force attack...")
    start_time = time.time()
    cracked_password = brute_force_attack(hash_to_crack, max_length=4)
    end_time = time.time()
    if cracked_password:
        print(f"Brute force attack successful! Password: {cracked_password}")
    else:
        print("Brute force attack failed.")
    print(f"Time taken: {end_time - start_time:.2f} seconds\n")

    # Demonstrate Dictionary Attack
    print("Starting dictionary attack...")
    start_time = time.time()
    # You need a dictionary file, here I'm using a small example list
    with open('dictionary.txt', 'w') as f:
        f.write('password\n123456\n123456789\nqwerty\nabc123\npassword1\n')
    cracked_password = dictionary_attack(hash_to_crack, 'dictionary.txt')
    end_time = time.time()
    if cracked_password:
        print(f"Dictionary attack successful! Password: {cracked_password}")
    else:
        print("Dictionary attack failed.")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

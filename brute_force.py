import hashlib
import itertools
import string

target_hash = input("Enter hash to crack: ")

chars = string.ascii_lowercase + string.digits

for length in range(1, 5):  # try up to 4 characters
    for attempt in itertools.product(chars, repeat=length):
        attempt = ''.join(attempt)
        hashed_attempt = hashlib.sha256(attempt.encode()).hexdigest()

        if hashed_attempt == target_hash:
            print("Password found:", attempt)
            exit()

print("Password not found")
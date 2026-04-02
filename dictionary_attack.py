import hashlib

target_hash = input("Enter hash: ")
found = False

with open("wordlist.txt", "r") as file:
    for word in file:
        word = word.strip()
        hashed_word = hashlib.sha256(word.encode()).hexdigest()

        if hashed_word == target_hash:
            print("Password found:", word)
            found = True
            break

if not found:
    print("Password not found in wordlist")
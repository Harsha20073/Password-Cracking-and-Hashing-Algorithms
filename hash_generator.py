import hashlib

password = input("Enter password: ")
# SHA-256 hashing
hashed = hashlib.sha256(password.encode()).hexdigest()

print("Hashed Password:", hashed)
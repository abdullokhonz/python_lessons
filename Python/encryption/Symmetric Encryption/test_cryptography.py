from cryptography.fernet import Fernet

# Generating a key
key = Fernet.generate_key()
cipher = Fernet(key)
print("Key: ", key)

# Encrypt message
message = b"Hello, cyber world!"
encrypted = cipher.encrypt(message)
print("Encrypted: ", encrypted)

# Decrypt message
decrypted = cipher.decrypt(encrypted)
print("Decrypted: ", decrypted)

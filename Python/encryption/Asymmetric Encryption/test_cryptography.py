from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# 1. Generate a key pair: private and public
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

print("Private key: ", private_key)
print("Public key: ", public_key)

# 2. Message for encryption
message = b"Secret message for you!"

print("Message: ", message.decode())

# 3. Encrypt the message using the PUBLIC key
encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("🔐 Encrypted:", encrypted)

# 4. Decrypt the message using the PRIVATE key
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("🔓 Decrypted:", decrypted)

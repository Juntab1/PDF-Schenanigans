import secrets

# Generate a random AES-256 key (32 bytes)
key = secrets.token_bytes(32)

# Convert the key to a hexadecimal string representation
key_hex = key.hex()

print(key_hex)  # This string can contain special characters
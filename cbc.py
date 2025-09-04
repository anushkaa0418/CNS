from Crypto.Cipher import AES # type: ignore
from Crypto.Random import get_random_bytes # type: ignore

def pad(t): 
    return t + b' ' * (16 - len(t) % 16)

def unpad(t):
    return t.rstrip(b' ')

# Key
key = input("Enter key (16/24/32 bytes): ").encode()[:32].ljust(32, b' ')

# IV
iv  = get_random_bytes(16)

# Message
msg = input("Enter message: ").encode()

# Encrypt
cipher_enc = AES.new(key, AES.MODE_CBC, iv)
enc = cipher_enc.encrypt(pad(msg))

# Decrypt
cipher_dec = AES.new(key, AES.MODE_CBC, iv)
dec = unpad(cipher_dec.decrypt(enc)).decode()

print("Key:", key)
print("IV:", iv)
print("Encrypted:", enc)
print("Decrypted:", dec)

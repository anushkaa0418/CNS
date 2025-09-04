#pip install pycryptodome
from Crypto.Cipher import DES # type: ignore

def pad(t):
    return t + b' ' * (8 - len(t) % 8)
def unpad(t):
    return t.rstrip(b' ')

key = input("Enter 8-byte key: ").encode()[:8].ljust(8, b' ')
msg = input("Enter text to encrypt: ").encode()

cipher = DES.new(key, DES.MODE_ECB)
enc = cipher.encrypt(pad(msg))
dec = unpad(cipher.decrypt(enc)).decode()

print("Encrypted:", enc)
print("Decrypted:", dec)

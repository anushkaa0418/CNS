from Crypto.Cipher import AES # type: ignore

def pad(t): 
    return t + b' ' * (16 - len(t) % 16)

def unpad(t):
    return t.rstrip(b' ')

key = input("Enter 16-byte key: ").encode()[:16].ljust(16, b' ')
msg = input("Enter message: ").encode()

cipher = AES.new(key, AES.MODE_ECB)
enc = cipher.encrypt(pad(msg))
dec = unpad(cipher.decrypt(enc)).decode()

print("Encrypted:", enc)
print("Decrypted:", dec)

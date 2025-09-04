def rc4(key, data):
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    out = []
    for c in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(c ^ S[(S[i] + S[j]) % 256])
    return bytes(out)

# Example
key = input("Enter key: ")
msg = input("Enter message: ").encode()
enc = rc4(key, msg)
dec = rc4(key, enc).decode()
print("Encrypted:", enc)
print("Decrypted:", dec)

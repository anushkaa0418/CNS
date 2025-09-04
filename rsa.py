# Simple RSA implementation
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

n = p * q
phi = (p - 1) * (q - 1)

# find e
for e in range(2, phi):
    if pow(e, 1, phi) != 0: break

# find d
for d in range(2, phi):
    if (e * d) % phi == 1: break

print(f"Public key: ({e}, {n})")
print(f"Private key: ({d}, {n})")

msg = int(input("Enter message (number): "))
enc = pow(msg, e, n)
dec = pow(enc, d, n)

print("Encrypted:", enc)
print("Decrypted:", dec)

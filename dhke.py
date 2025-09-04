# Diffie-Hellman Key Exchange
p = int(input("Enter prime modulus p: "))
g = int(input("Enter base g: "))

a = int(input("Alice's private key a: "))
b = int(input("Bob's private key b: "))

A, B = pow(g, a, p), pow(g, b, p)  # public keys
sa, sb = pow(B, a, p), pow(A, b, p)  # shared secrets

print(f"Alice's public key: {A}")
print(f"Bob's public key:   {B}")

print("Shared secret computed by Alice:", sa)
print("Shared secret computed by Bob:", sb)
if sa == sb:
    print("Success! Both shared secrets match.")
else:
    print("Error! Shared secrets do not match.")


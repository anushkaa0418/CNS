def encrypt(text, s):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + s) % 26 + base)
        else:
            result += char 
    return result

def decrypt(text, s):
    return encrypt(text, -s)


text = input("Enter text: ")
s = int(input("Enter shift key: "))

encrypted = encrypt(text, s)
decrypted = decrypt(encrypted, s)

print("\nText:", text)
print("Shift:", s)
print("Cipher:", encrypted)
print("Decrypted:", decrypted)

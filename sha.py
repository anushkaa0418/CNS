import hashlib
my_text = input("Enter a message: ")
my_bytes = my_text.encode('utf-8')
hash_object = hashlib.sha512()
hash_object.update(my_bytes)
hash_hex = hash_object.hexdigest()
print("SHA-512 hash of", my_text, ":", hash_hex)
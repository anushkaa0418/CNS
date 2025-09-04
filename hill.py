import numpy as np

def mod_inverse(a, m):
    return next((i for i in range(1, m) if (a*i) % m == 1), None)

def matrix_mod_inv(matrix, m):
    n = matrix.shape[0]
    det = int(round(np.linalg.det(matrix))) % m
    det_inv = mod_inverse(det, m)
    if det_inv is None:
        raise ValueError("Matrix not invertible mod", m)

    # Compute adjugate matrix with integers
    cofactors = np.zeros((n,n), dtype=int)
    for r in range(n):
        for c in range(n):
            minor = np.delete(np.delete(matrix, r, axis=0), c, axis=1)
            cofactors[r, c] = ((-1)**(r+c) * int(round(np.linalg.det(minor)))) % m

    adj = cofactors.T % m
    return (det_inv * adj) % m

to_nums = lambda text: [ord(c)-97 for c in text.lower() if c.isalpha()]
to_text = lambda nums: ''.join(chr(n%26+97) for n in nums)

def pad(nums, n):
    while len(nums) % n != 0:
        nums.append(ord('x')-97)
    return nums

def hill_encrypt(msg, key):
    n, nums, out = key.shape[0], pad(to_nums(msg), key.shape[0]), ""
    for i in range(0,len(nums),n): out += to_text(key.dot(nums[i:i+n])%26)
    return out

def hill_decrypt(cipher, key, orig_len):
    n, nums, out = key.shape[0], to_nums(cipher), ""
    inv = matrix_mod_inv(key, 26)
    for i in range(0,len(nums),n): out += to_text(inv.dot(nums[i:i+n])%26)
    return out[:orig_len], inv

if __name__ == "__main__":
    size = int(input("Enter size of key matrix: "))
    key = np.array(list(map(int,input(f"Enter {size*size} numbers: ").split()))).reshape(size,size)
    msg = input("Enter a message (lowercase): ")
    enc = hill_encrypt(msg, key)
    dec, inv = hill_decrypt(enc, key, len(to_nums(msg)))
    print("Encrypted string is:", enc)
    print("Inverse matrix mod 26 is:\n", inv)
    print("Decrypted string is:", dec)

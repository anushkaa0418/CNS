def prepare_text(text, for_encryption):
    text = text.upper().replace("J", "I").replace(" ", "")
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"
        if for_encryption and a == b:
            pairs.append((a, "X"))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    return pairs

def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c.isalpha() and c not in matrix:
            matrix.append(c)
    matrix_5x5 = [matrix[i:i+5] for i in range(0, 25, 5)]
    pos = {matrix[i]: (i // 5, i % 5) for i in range(25)}  # lookup table
    return matrix_5x5, pos

def process_pair(pair, matrix, pos, shift):
    a, b = pair
    r1, c1 = pos[a]
    r2, c2 = pos[b]
    if r1 == r2:  # same row
        return matrix[r1][(c1 + shift) % 5] + matrix[r2][(c2 + shift) % 5]
    elif c1 == c2:  # same column
        return matrix[(r1 + shift) % 5][c1] + matrix[(r2 + shift) % 5][c2]
    else:  # rectangle swap
        return matrix[r1][c2] + matrix[r2][c1]

def encrypt(text, matrix, pos):
    return "".join(process_pair(p, matrix, pos, 1) for p in prepare_text(text, True))

def decrypt(cipher, matrix, pos):
    return "".join(process_pair(p, matrix, pos, -1) for p in prepare_text(cipher, False))


# --- Main Program ---
text = input("Enter text: ")
key = input("Enter key: ")

matrix, pos = create_matrix(key)
print("Key Matrix:")
for row in matrix:
    print(" ".join(row))

cipher = encrypt(text, matrix, pos)
print("Encrypted:", cipher)
print("Decrypted:", decrypt(cipher, matrix, pos))

def encrypt(msg, rails, cols):
    # --- Rail Fence ---
    rail, step, fence = 0, 1, [''] * rails
    for c in msg.replace(" ", ""):   # remove spaces for consistency
        fence[rail] += c
        rail += step
        if rail in (0, rails-1): step *= -1
    rf = ''.join(fence)

    # --- Row/Column Transposition ---
    while len(rf) % cols: rf += 'X'
    grid = [rf[i:i+cols] for i in range(0, len(rf), cols)]
    return ''.join(''.join(row[c] for row in grid) for c in range(cols))

def decrypt(cipher, rails, cols):
    # --- Reverse Row/Column ---
    rows, i = len(cipher)//cols, 0
    grid = [['']*cols for _ in range(rows)]
    for c in range(cols):
        for r in range(rows):
            grid[r][c] = cipher[i]; i+=1
    plain = ''.join(''.join(row) for row in grid)

    # --- Reverse Rail Fence ---
    pattern, rail, step = [], 0, 1
    for _ in plain:
        pattern.append(rail)
        rail += step
        if rail in (0, rails-1): step *= -1
    counts = [pattern.count(r) for r in range(rails)]
    parts, i = [], 0
    for c in counts:
        parts.append(list(plain[i:i+c])); i+=c
    idx, out = [0]*rails, ''
    for r in pattern:
        out += parts[r][idx[r]]; idx[r]+=1
    return out.rstrip('X')

msg = input("Enter Message: ")
rails = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
enc = encrypt(msg, rails, cols)
dec = decrypt(enc, rails, cols)
print("Encrypted:", enc)
print("Decrypted:", dec)

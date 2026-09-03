# Generate Key
def generateKey(text, key):
    key = key.upper()
    while len(key) < len(text):
        key += key
    return key[:len(text)]


# Encryption
def encrypt(text, key):
    cipher = ""
    for i in range(len(text)):
        x = (ord(text[i]) - 65 + ord(key[i]) - 65) % 26
        cipher += chr(x + 65)
    return cipher


# Decryption
def decrypt(cipher, key):
    plain = ""
    for i in range(len(cipher)):
        x = (ord(cipher[i]) - 65 - (ord(key[i]) - 65)) % 26
        plain += chr(x + 65)
    return plain


# Main Program
plain = input("Enter Plaintext: ").upper()
keyword = input("Enter Keyword: ")

key = generateKey(plain, keyword)

cipher = encrypt(plain, key)
print("Generated Key:", key)
print("Ciphertext:", cipher)

original = decrypt(cipher, key)
print("Decrypted:", original)

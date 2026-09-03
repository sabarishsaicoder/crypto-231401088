import numpy as np

# Key matrix
key = np.array([[3, 3],
                [2, 5]])

# Inverse key matrix (mod 26)
inverse = np.array([[15, 17],
                    [20, 9]])

# Process plaintext
def process(text):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"
    return text

# Convert letters to numbers
def convert(text):
    return [ord(i) - 65 for i in text]

# Encryption
def encrypt(text):
    text = process(text)
    nums = convert(text)
    cipher = ""

    for i in range(0, len(nums), 2):
        pair = np.array([[nums[i]],
                         [nums[i + 1]]])

        result = np.dot(key, pair) % 26
        cipher += chr(result[0][0] + 65)
        cipher += chr(result[1][0] + 65)

    return cipher

# Decryption
def decrypt(cipher):
    nums = convert(cipher)
    plain = ""

    for i in range(0, len(nums), 2):
        pair = np.array([[nums[i]],
                         [nums[i + 1]]])

        result = np.dot(inverse, pair) % 26
        plain += chr(result[0][0] + 65)
        plain += chr(result[1][0] + 65)

    return plain

# Main Program
plain = input("Enter Plaintext: ")

cipher = encrypt(plain)
print("Ciphertext :", cipher)

decrypted = decrypt(cipher)
print("Decrypted  :", decrypted)

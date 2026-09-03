p = 7
q = 11
seed = 16
num_bits = 5

n = p * q


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if gcd(seed, n) != 1:
    print("Invalid seed")
else:
    x = seed
    bits = []

    print("Blum Blum Shub Generator")
    print("------------------------")

    for i in range(num_bits):
        x = (x * x) % n
        bit = x % 2
        bits.append(bit)

        print("Random number =", x, "Output bit =", bit)

    print("\nGenerated Bits:", bits)

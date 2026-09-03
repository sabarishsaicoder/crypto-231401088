def findGCD(a, b):
    if a < b:
        a, b = b, a

    print("\nSteps of Euclidean Algorithm:")

    while b != 0:
        remainder = a % b
        print(f"{a} / {b} = Quotient {a // b}, Remainder {remainder}")
        a = b
        b = remainder

    return a


print("=== Secure Communication Key Validation ===")

p1 = int(input("Enter the 1st encryption parameter: "))
p2 = int(input("Enter the 2nd encryption parameter: "))

gcd = findGCD(p1, p2)

print("GCD =", gcd)

if gcd == 1:
    print("\nThe encryption parameters are coprime.")
    print("Secure communication can be established.")
else:
    print("\nThe encryption parameters are NOT coprime.")
    print("Communication setup rejected.")
    print("Choose different encryption parameters.")

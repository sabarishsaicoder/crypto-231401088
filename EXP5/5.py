import hashlib
 
p, q, g = 23, 11, 4
x = 3                     # Private Key
y = pow(g, x, p)          # Public Key
k = 7                     # Random Number
 
m = input("Enter Message: ")
h = int(hashlib.sha256(m.encode()).hexdigest(), 16) % q
 
# Signature Generation
r = pow(g, k, p) % q
s = (pow(k, -1, q) * (h + x * r)) % q
print("Signature =", (r, s))
 
# Signature Verification
w = pow(s, -1, q)
u1 = (h * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
print("Verification Value =", v)
 
if v == r:
    print("Signature Valid")
else:
    print("Signature Invalid")

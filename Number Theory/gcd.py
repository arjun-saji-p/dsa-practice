a = 12
b = 18

while b:
    a, b = b, a % b

print("GCD =", a)

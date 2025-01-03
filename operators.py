# Arithmetic Operators
a, b = 10, 3
print("Arithmetic Operators:")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}\n")

# Assignment Operators
c = 5
print("Assignment Operators:")
c += 2; print(f"c += 2: {c}")
c -= 1; print(f"c -= 1: {c}")
c *= 3; print(f"c *= 3: {c}")
c /= 2; print(f"c /= 2: {c}")
c //= 2; print(f"c //= 2: {c}")
c %= 3; print(f"c %= 3: {c}")
c **= 2; print(f"c **= 2: {c}\n")

# Comparison Operators
print("Comparison Operators:")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}\n")

# Logical Operators
x, y = True, False
print("Logical Operators:")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}\n")

# Bitwise Operators
print("Bitwise Operators:")
print(f"a & b: {a & b}")
print(f"a | b: {a | b}")
print(f"a ^ b: {a ^ b}")
print(f"~a: {~a}")
print(f"a << 2: {a << 2}")
print(f"a >> 2: {a >> 2}\n")

# Membership Operators
list_example = [1, 2, 3, 4, 5]
print("Membership Operators:")
print(f"3 in list_example: {3 in list_example}")
print(f"6 not in list_example: {6 not in list_example}\n")

# Identity Operators
print("Identity Operators:")
x1, x2 = [1, 2, 3], [1, 2, 3]
print(f"x1 is x2: {x1 is x2}")
print(f"x1 is not x2: {x1 is not x2}")
x3 = x1
print(f"x1 is x3: {x1 is x3}")

# Task 7: Operators
# Arithmetic, logical, identity/membership operators

x, y = 17, 5
print(x + y, x - y, x * y, x / y, x // y, x % y, x ** y)

print(bool(x > y and x < y))
print(bool(x > y or x < y))
print(bool(not (x > y or x < y)))

x = "bangladesh"
print("b" in x)

a, b = "nabil", "nabil"
print(a is b)

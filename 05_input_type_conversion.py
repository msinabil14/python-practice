# Task 5: Input and Type Conversion

# Without conversion (strings get concatenated, not added)
a = "10"
b = "12"
print(a + b)

# Fixed with int() conversion
print(int(a) + int(b))

# Take name and age, print next year's age
name = input("name : ")
age = int(input("age : "))
print("your name is :", name, ".", "next year you will be:", age + 1)

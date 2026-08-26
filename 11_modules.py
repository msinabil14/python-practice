# Task 11: Modules (math, random)

import math
pi = math.pi
r = float(input("Enter the radius of circle : "))
print("The area of circle is :", pi * r * r)

import random
names = ["nabil", "zisan", "zihad", "nafsi", "shahat"]
random.shuffle(names)
print(names)

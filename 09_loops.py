# Task 9: Loops (while, for, nested, break/continue/pass)

# While loop - multiplication table
num = int(input("Enter a num: "))
for i in range(1, 11):
    print(num, "*", i, "=", num * i)

# Guessing game
import random
jackpot = random.randint(1, 100)
guess = int(input("Guess a number within 1 to 100 : "))

while guess != jackpot:
    if guess < jackpot:
        print("Guess higher")
    elif guess > jackpot:
        print("Guess lower")
    guess = int(input("Guess a number within 1 to 100 : "))

print("JACKPOT..!!")

# Even numbers from 2 to 50
for i in range(2, 51, 2):
    print(i)

# Sequence loop
for i in "Bangladesh":
    print(i)

# Nested loop - number pyramid
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Break / Continue example
for i in range(1, 21):
    if i % 3 == 0:
        continue
    if i == 15:
        break
    print(i)

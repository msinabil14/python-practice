# Task 8: Conditionals and Indentation

# Login system with retry logic
username = input("Enter Your Username : ")
password = input("Enter Your password : ")

if username == "msinabil14" and password == "1234":
    print("Welcome")
elif username == "msinabil14" and password != "1234":
    print("Wrong Password")
    password = input("Enter Your password : ")
    if password == "1234":
        print("Welcome")
    else:
        print("Wrong Password")
else:
    print("Cannot login")

# Positive / negative / zero checker
num = int(input("Enter a int num : "))

if num > 0:
    print("positive number")
elif num < 0:
    print("negative number")
else:
    print("Zero")

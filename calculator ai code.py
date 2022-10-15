#simple calculator python using pycharm run code

#!/usr/bin/env python3

# This is a simple calculator program written in Python

# Define our functions

def add(x, y):

    print("""This function adds two numbers""")

    return x + y

def subtract(x, y):

    print("""This function subtracts two numbers""")

    return x - y

def multiply(x, y):

    print("""This function multiplies two numbers""")

    return x * y

def divide(x, y):

    print("""This function divides two numbers""")

    return x / y

# Main program

print("Welcome to the simple calculator")

operation = input("What would you like to do?\n")

print("1) Add\n")

print("2) Subtract\n")

print("3) Multiply\n")

print("4) Divide\n")

if operation == '1':

    num1 = float(input("Enter the first number: "))

    num2 = float(input("Enter the second number: "))

    result = add(num1, num2)

elif operation == '2':

    num1 = float(input("Enter the first number: "))

    num2 = float(input("Enter the second number: "))

    result = subtract(num1, num2)

elif operation == '3':

    num1 = float(input("Enter the first number: "))

    num2 = float(input("Enter the second number: "))

    result = multiply(num1, num2)

elif operation == '4':

    num1 = float(input("Enter the first number: "))

    num2 = float(input("Enter the second number: "))

    result = divide(num1, num2)

else:

    print("Invalid input")

# Print the result

print("the result is:", result)
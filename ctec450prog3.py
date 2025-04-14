import math

def factorial_function(num):
    if num == 0:
        return 1
    else:
        return num * factorial_function(num - 1)

try:
    num = int(input("Enter a positive number: "))

    if num >= 0:
        print("The factorial of", num, "is", factorial_function(num))
    else:
        print("Invalid input. Please enter a posiive number.")

except ValueError:
    print("Invalid input. Only enter a positive number.")
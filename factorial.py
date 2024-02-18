import math

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = math.factorial(num)
    print(f"The factorial of {num} is {result}")

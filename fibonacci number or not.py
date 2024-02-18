import math
def is_perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num

def is_fibonacci(n):
    if n < 0:
        return False

    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

number_to_check = int(input("Enter a number to check if it's a Fibonacci number: "))

if is_fibonacci(number_to_check):
    print(number_to_check, "is a Fibonacci number.")
else:
    print(number_to_check, "is not a Fibonacci number.")
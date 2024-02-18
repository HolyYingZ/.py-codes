def find_nth_multiple_in_fibonacci(n, multiple):
    a, b = 0, 1
    count = 0

    while True:
        if a % multiple == 0:
            count += 1

        if count == n:
            return a

        a, b = b, a + b
n = int(input("Enter the value of n for the nth multiple: "))
multiple = int(input("Enter the number to find multiples in the Fibonacci series: "))

result = find_nth_multiple_in_fibonacci(n, multiple)
print(f"The {n}th multiple of {multiple} in the Fibonacci series is: {result}")
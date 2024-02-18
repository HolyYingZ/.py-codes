def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
n = int(input("Enter the value of n for the nth Fibonacci number: "))
result = fibonacci(n)
print("The fibonacci number is:",result)
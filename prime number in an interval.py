def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
start_interval = int(input("Enter the start of the interval: "))
end_interval = int(input("Enter the end of the interval: "))

print(f"Prime numbers in the interval [{start_interval}, {end_interval}]:")
for num in range(start_interval, end_interval + 1):
    if is_prime(num):
        print(num)
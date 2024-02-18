def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)

    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    

    return armstrong_sum == number

# Example usage
number_to_check = int(input("Enter a number to check if it's an Armstrong number: "))

result = "is" if is_armstrong_number(number_to_check) else "is not"
print(f"{number_to_check} {result} an Armstrong number.")
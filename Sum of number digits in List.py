def sum_of_digits_in_list(numbers_list):
    total_sum = 0
    for number in numbers_list:
        num_str = str(number)
        for digit in num_str:
            total_sum += int(digit)
    return total_sum
numbers_list = [123, 45, 678, 9]
result = sum_of_digits_in_list(numbers_list)
print("Original list:", numbers_list)
print("Sum of digits in the list:", result)

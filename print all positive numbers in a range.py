def print_positive_numbers_in_range(start, end):
    positive_numbers = [num for num in range(start, end + 1) if num > 0]
    if positive_numbers:
        print("Positive numbers in the range:", positive_numbers)
    else:
        print("No positive numbers in the specified range.")

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
print_positive_numbers_in_range(start_range, end_range)

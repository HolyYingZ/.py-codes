def print_negative_numbers_in_range(start, end):
    negative_numbers = [num for num in range(start, end + 1) if num < 0]
    if negative_numbers:
        print(f"Negative numbers in the range ({start} to {end}): {negative_numbers}")
    else:
        print("No negative numbers in the specified range.")
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
print_negative_numbers_in_range(start_range, end_range)

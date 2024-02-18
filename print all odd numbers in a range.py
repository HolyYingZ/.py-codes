def print_odd_numbers_in_range(start, end):
    odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]
    if odd_numbers:
        print("Odd numbers in the range:", odd_numbers)
    else:
        print("No odd numbers in the specified range.")

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
print_odd_numbers_in_range(start_range, end_range)

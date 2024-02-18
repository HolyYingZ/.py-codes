def print_even_numbers_in_range(start, end):
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    if even_numbers:
        print("Even numbers in the range:", even_numbers)
    else:
        print("No even numbers in the specified range.")
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
print_even_numbers_in_range(start_range, end_range)

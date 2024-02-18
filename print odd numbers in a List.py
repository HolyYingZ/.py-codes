def print_odd_numbers(my_list):
    odd_numbers = [num for num in my_list if num % 2 != 0]
    if odd_numbers:
        print("Odd numbers in the list:", odd_numbers)
    else:
        print("No odd numbers in the list.")
\
num_list = [int(x) for x in input("Enter elements of the list separated by spaces: ").split()]
print_odd_numbers(num_list)

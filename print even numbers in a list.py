def print_even_numbers(my_list):
    even_numbers = [num for num in my_list if num % 2 == 0]
    if even_numbers:
        print("Even numbers in the list:", even_numbers)
    else:
        print("No even numbers in the list.")

# Input from the user
num_list = [int(x) for x in input("Enter elements of the list separated by spaces: ").split()]
print_even_numbers(num_list)

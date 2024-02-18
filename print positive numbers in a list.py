def print_positive_numbers(my_list):
    positive_numbers = [num for num in my_list if num > 0]
    if positive_numbers:
        print("Positive numbers in the list:", positive_numbers)
    else:
        print("No positive numbers in the list.")

num_list = [int(x) for x in input("Enter elements of the list separated by spaces: ").split()]
print_positive_numbers(num_list)

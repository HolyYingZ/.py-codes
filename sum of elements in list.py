def sum_of_elements(my_list):
    return sum(my_list)

num_list = [int(x) for x in input("Enter elements of the list: ").split()]

result = sum_of_elements(num_list)
print(f"The sum of elements in the list is: {result}")

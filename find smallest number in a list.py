def find_smallest_number(my_list):
    if not my_list:
        return None 
    else:
        return min(my_list)

num_list = [int(x) for x in input("Enter elements of the list: ").split()]
result = find_smallest_number(num_list)

if result is not None:
    print(f"The smallest number in the list is: {result}")
else:
    print("The list is empty.")

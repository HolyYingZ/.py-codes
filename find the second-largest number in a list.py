def find_second_largest_number(my_list):
    if len(my_list) < 2:
        return None  
    else:
        sorted_list = sorted(set(my_list), reverse=True)
        return sorted_list[1]


num_list = [int(x) for x in input("Enter elements of the list: ").split()]

result = find_second_largest_number(num_list)

if result is not None:
    print(f"The second largest number in the list is: {result}")
else:
    print("The list has less than two elements.")

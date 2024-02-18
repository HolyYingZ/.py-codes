def multiply_list_elements(my_list):
    result = 1
    for num in my_list:
        result *= num
    return result

# Input from the user
num_list = [int(x) for x in input("Enter elements of the list: ").split()]
result = multiply_list_elements(num_list)
print(f"The product of elements in the list is: {result}")

def sort_values_using_key(first_list, second_list):
    combined_lists = zip(second_list, first_list)
    sorted_combined = sorted(combined_lists)
    sorted_values = [value for key, value in sorted_combined]
    
    return sorted_values

values_list = [3, 1, 4, 2]
key_list = ['apple', 'banana', 'cherry', 'date']

result = sort_values_using_key(values_list, key_list)

print("Original values list:", values_list)
print("Key list:", key_list)
print("Values list sorted based on the key list:", result)

def unique_values(dictionary):
    unique_values_set = set(value for values in dictionary.values() for value in values)
    return list(unique_values_set)

# Example dictionary
my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}

# Extract unique values from dictionary values
result = unique_values(my_dict)

# Display the result
print("Original Dictionary:")
print(my_dict)
print("Unique Values from Dictionary Values:", result)

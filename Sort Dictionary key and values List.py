my_dict = {'b': [20, 25], 'a': [10, 15], 'c': [30, 35]}

sorted_dict = {key: sorted(values) for key, values in my_dict.items()}

print("Original Dictionary:")
print(my_dict)
print("Sorted Dictionary key and values list:")
print(sorted_dict)

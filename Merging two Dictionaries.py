# Method 1: Using the update() method
dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40}
dict1.update(dict2)

# Method 2: Using the {**dict1, **dict2} syntax (Python 3.5+)
dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40}
merged_dict = {**dict1, **dict2}

# Display the result
print("Original Dictionaries:")
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:")
print("Using update():", dict1)
print("Using {**dict1, **dict2} syntax:", merged_dict)

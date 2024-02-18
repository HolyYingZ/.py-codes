my_dict = {'a': 10, 'b': 20, 'c': 30}
keys_associated_with_values = [key for key, value in my_dict.items() if value == 20]
print("Original Dictionary:")
print(my_dict)
print("Keys Associated with Value 20:", keys_associated_with_values)

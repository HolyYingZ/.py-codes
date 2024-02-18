my_dict = {'b': 20, 'a': 10, 'c': 30}

sorted_by_key = dict(sorted(my_dict.items()))
sorted_by_value = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("Original Dictionary:")
print(my_dict)
print("Sorted Dictionary by Key:")
print(sorted_by_key)
print("Sorted Dictionary by Value:")
print(sorted_by_value)

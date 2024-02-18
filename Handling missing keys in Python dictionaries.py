my_dict = {'a': 10, 'b': 20, 'c': 30}

value = my_dict.get('d', 'Key not found')

from collections import defaultdict
default_dict = defaultdict(lambda: 'Key not found', my_dict)
value_default = default_dict['d']

print("Original Dictionary:")
print(my_dict)
print("Handling missing keys using get():", value)
print("Handling missing keys using defaultdict:", value_default)

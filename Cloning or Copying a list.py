#Method 1: Using Slicing
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]

print("Original list:", original_list)
print("Cloned list using slicing:", cloned_list)

#Method 2: Using list() constructor
original_list = [1, 2, 3, 4, 5]
cloned_list = list(original_list)
print("Original list:", original_list)
print("Cloned list using list() constructor:", cloned_list)

#Method 3: Using copy() method
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list.copy()
print("Original list:", original_list)
print("Cloned list using copy() method:", cloned_list)

#Method 4: Using copy module
from copy import copy
original_list = [1, 2, 3, 4, 5]
cloned_list = copy(original_list)
print("Original list:", original_list)
print("Cloned list using copy() function:", cloned_list)
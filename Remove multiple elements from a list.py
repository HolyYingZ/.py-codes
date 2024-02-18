#Method 1: Using List Comprehension
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
elements_to_remove = [2, 4, 6]
updated_list = [num for num in my_list if num not in elements_to_remove]
print("Original list:", my_list)
print("List after removing elements:", updated_list)

#Method 2: Using remove() method
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

elements_to_remove = [2, 4, 6]
for element in elements_to_remove:
    my_list.remove(element)
print("Original list:", my_list)

#Method 3: Using filter() function
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
elements_to_remove = [2, 4, 6]
updated_list = list(filter(lambda num: num not in elements_to_remove, my_list))
print("Original list:", my_list)
print("List after removing elements:", updated_list)
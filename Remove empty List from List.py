#Method 1: Using List Comprehension
my_list = [1, [], [3, 4], [], 5, [], []]
updated_list = [sublist for sublist in my_list if sublist]
print("Original list:", my_list)
print("List after removing empty lists:", updated_list)

#Method 2: Using filter() function
my_list = [1, [], [3, 4], [], 5, [], []]
updated_list = list(filter(lambda sublist: sublist, my_list))
print("Original list:", my_list)
print("List after removing empty lists:", updated_list)
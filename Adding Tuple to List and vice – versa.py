my_list = [(1, 2), (3, 4), (5, 6)]
my_tuple = (7, 8)
list_with_added_tuple = my_list + [my_tuple]
tuple_with_added_list = tuple(my_list) + (my_tuple,)
print("Original List:", my_list)
print("Tuple to be Added:", my_tuple)
print("List with Added Tuple:", list_with_added_tuple)
print("\nOriginal Tuple:", my_tuple)
print("List to be Added:", my_list)
print("Tuple with Added List:", tuple_with_added_list)

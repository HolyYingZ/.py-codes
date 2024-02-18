tuple_of_list = ([1, 2], [3, 4], [5, 6])
flattened_tuple = tuple(item for sublist in tuple_of_list for item in sublist)
print("Original Tuple of List:", tuple_of_list)
print("Flattened Tuple:", flattened_tuple)

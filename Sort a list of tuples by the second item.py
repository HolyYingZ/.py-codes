tuple_list = [(1, 3), (2, 1), (3, 5), (4, 2), (5, 4)]
sorted_tuple_list = sorted(tuple_list, key=lambda x: x[1])
print("Original List of Tuples:", tuple_list)
print("Sorted List of Tuples by Second Item:", sorted_tuple_list)

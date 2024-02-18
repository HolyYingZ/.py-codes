tuple_list = [(1, 'x'), (3, 'z'), (2, 'y')]
order_list = [2, 3, 1]
ordered_tuple_list = [tuple_list[i - 1] for i in order_list]
print("Original List of Tuples:", tuple_list)
print("External Order List:", order_list)
print("Ordered List of Tuples:", ordered_tuple_list)

tuple_list = [(1, 2), (3, 4, 5), (6,), (7, 8), (9, 10, 11)]
k = 2
filtered_tuple_list = [tup for tup in tuple_list if len(tup) != k]
print("Original Tuple List:", tuple_list)
print(f"Remove Tuples of Length {k}:", filtered_tuple_list)

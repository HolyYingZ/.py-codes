my_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
k = 3
max_k_elements = tuple(sorted(my_tuple)[-k:])
min_k_elements = tuple(sorted(my_tuple)[:k])
print("Original Tuple:", my_tuple)
print(f"Maximum {k} elements:", max_k_elements)
print(f"Minimum {k} elements:", min_k_elements)

my_tuple = ((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))
k = 2
closest_pair = min(my_tuple, key=lambda x: abs(x[0] - my_tuple[k][0]) + abs(x[1] - my_tuple[k][1]))
print("Original Tuple:", my_tuple)
print(f"Closest Pair to Kth index element ({k}):", closest_pair)

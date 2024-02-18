my_tuple = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e')]
result_dict = {}
for tup in my_tuple:
    result_dict.setdefault(tup[0], []).append(tup[1])
result_tuple = [(key, *values) for key, values in result_dict.items()]
print("Original Tuple:", my_tuple)
print("Joined Tuples with Similar Initial Element:", result_tuple)

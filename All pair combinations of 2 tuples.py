tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
pair_combinations = [(x, y) for x in tuple1 for y in tuple2]
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("All Pair Combinations of 2 Tuples:", pair_combinations)

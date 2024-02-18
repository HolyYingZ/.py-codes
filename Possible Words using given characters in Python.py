from itertools import permutations
characters = 'abc'
possible_words = [''.join(perm) for perm in permutations(characters)]
print("Given Characters:", characters)
print("Possible Words using Given Characters:")
print(possible_words)

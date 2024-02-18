from itertools import permutations
string = input("Enter a string: ")
permutations_result = [''.join(perm) for perm in permutations(string)]
print("Permutations of the string:")
for perm in permutations_result:
    print(perm)

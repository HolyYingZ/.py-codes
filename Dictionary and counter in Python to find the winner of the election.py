from collections import Counter
votes = ['John', 'Alice', 'Bob', 'John', 'Alice', 'Bob', 'John', 'Alice']

winner = Counter(votes).most_common(1)[0][0]

print("Votes List:", votes)
print("Winner of the Election:", winner)

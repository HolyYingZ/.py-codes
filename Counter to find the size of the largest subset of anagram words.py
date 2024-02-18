from collections import Counter

words = ['listen', 'silent', 'enlist', 'eat', 'tea', 'ate']
anagram_counter = Counter([''.join(sorted(word)) for word in words])
largest_subset_size = max(anagram_counter.values())
print("List of Words:")
print(words)
print("Size of the Largest Subset of Anagram Words:", largest_subset_size)

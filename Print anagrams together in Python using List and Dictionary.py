words = ['listen', 'silent', 'enlist', 'eat', 'tea', 'ate']

anagrams_dict = {}
for word in words:
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagrams_dict:
        anagrams_dict[sorted_word].append(word)
    else:
        anagrams_dict[sorted_word] = [word]

# Display the result
print("List of Words:")
print(words)
print("Anagrams Grouped Together:")
print(list(anagrams_dict.values()))

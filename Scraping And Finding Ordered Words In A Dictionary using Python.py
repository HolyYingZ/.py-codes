my_dict = {'apple': 10, 'banana': 20, 'cherry': 30}
ordered_words = [word for word in my_dict.keys() if ''.join(sorted(word)) == word]
print("Original Dictionary:")
print(my_dict)
print("Ordered Words in the Dictionary:", ordered_words)

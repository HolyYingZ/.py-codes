from collections import Counter
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency_dict = dict(Counter(my_list))
are_frequencies_same = len(set(frequency_dict.values())) == 1
print("Original List:", my_list)
print("Frequencies of Items in the List:", frequency_dict)
print("Can Frequencies Become the Same?", are_frequencies_same)

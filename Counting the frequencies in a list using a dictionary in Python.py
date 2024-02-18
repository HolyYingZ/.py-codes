my_list = [1, 2, 3, 1, 2, 3, 4, 1, 2]
frequency_dict = {}
for item in my_list:
    frequency_dict[item] = frequency_dict.get(item, 0) + 1

print("Original List:", my_list)
print("Frequencies of Items in the List:", frequency_dict)

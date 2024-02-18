from collections import Counter

def least_frequent_character(s):
    char_count = Counter(s)
    least_frequent_char = min(char_count, key=char_count.get)
    return least_frequent_char


string = input("Enter a string: ")

result = least_frequent_character(string)

print("Original String:", string)
print("Least frequent character:", result)

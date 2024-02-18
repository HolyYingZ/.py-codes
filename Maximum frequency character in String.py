from collections import Counter
def most_frequent_character(s):
    char_count = Counter(s)
    most_frequent_char = max(char_count, key=char_count.get)
    return most_frequent_char
string = input("Enter a string: ")
result = most_frequent_character(string)
print("Original String:", string)
print("Most frequent character:", result)

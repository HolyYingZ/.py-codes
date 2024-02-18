from collections import Counter

def find_duplicate_characters(s):
    char_count = Counter(s)
    duplicates = [char for char, count in char_count.items() if count > 1]
    return duplicates
string = input("Enter a string: ")

result = find_duplicate_characters(string)
print("Original String:", string)
print("Duplicate characters in the string:", result)

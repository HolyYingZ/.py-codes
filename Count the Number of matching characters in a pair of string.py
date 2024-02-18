def count_matching_characters(str1, str2):
    matching_characters = set(str1) & set(str2)
    return len(matching_characters)
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = count_matching_characters(string1, string2)
print("First string:", string1)
print("Second string:", string2)
print("Number of matching characters:", result)

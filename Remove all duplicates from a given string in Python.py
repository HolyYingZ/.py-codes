def remove_duplicates(s):
    unique_chars = set()
    result = ''
    for char in s:
        if char not in unique_chars:
            result += char
            unique_chars.add(char)
    return result

string = input("Enter a string: ")

result = remove_duplicates(string)

print("Original String:", string)
print("String after removing duplicates:", result)

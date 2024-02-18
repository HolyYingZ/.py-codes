def replace_substring(s, old_substring, new_substring):
    return s.replace(old_substring, new_substring)

string = input("Enter a string: ")
old_substring = input("Enter the old substring to replace: ")
new_substring = input("Enter the new substring: ")
result = replace_substring(string, old_substring, new_substring)

print("Original String:", string)
print(f"String after replacing '{old_substring}' with '{new_substring}':", result)

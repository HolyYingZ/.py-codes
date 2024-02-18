def remove_ith_character(s, i):
    return s[:i] + s[i+1:]
string = input("Enter a string: ")
index = int(input("Enter the index to remove: "))
result = remove_ith_character(string, index)

print("Original String:", string)
print(f"String after removing character at index {index}:", result)

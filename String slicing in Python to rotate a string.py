def rotate_string(s, k):
    return s[k:] + s[:k]
string = input("Enter a string: ")
rotation_count = int(input("Enter the rotation count: "))
result = rotate_string(string, rotation_count)
print("Original String:", string)
print(f"String after rotating {rotation_count} positions:", result)

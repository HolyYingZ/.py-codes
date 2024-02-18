def is_binary_string(s):
    return all(char in '01' for char in s)
string = input("Enter a string: ")

if is_binary_string(string):
    print(f"The string '{string}' is a binary string.")
else:
    print(f"The string '{string}' is not a binary string.")

def split_and_join(s):
    words = s.split()
    joined_string = '-'.join(words)
    return joined_string

string = input("Enter a string: ")

result = split_and_join(string)

print("Original String:", string)
print("String after split and join:", result)

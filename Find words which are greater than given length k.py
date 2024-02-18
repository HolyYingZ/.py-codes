def words_greater_than_length(s, k):
    words = s.split()
    result = [word for word in words if len(word) > k]
    return result
string = input("Enter a string: ")
length = int(input("Enter the minimum length (k): "))

result = words_greater_than_length(string, length)

print("Original String:", string)
print(f"Words greater than length {length}:", result)

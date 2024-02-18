def reverse_words(s):
    words = s.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string
string = input("Enter a string: ")
result = reverse_words(string)
print("Original String:", string)
print("String with reversed words:", result)

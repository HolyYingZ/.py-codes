def even_length_words(s):
    words = s.split()
    even_length_words_list = [word for word in words if len(word) % 2 == 0]
    return even_length_words_list
string = input("Enter a string: ")

result = even_length_words(string)

print("Original String:", string)
print("Even length words in the string:", result)

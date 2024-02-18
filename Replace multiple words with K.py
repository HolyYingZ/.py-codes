def replace_multiple_words(s, words_to_replace, replacement):
    for word in words_to_replace:
        s = s.replace(word, replacement)
    return s

string = input("Enter a string: ")
words_to_replace = input("Enter words to replace (comma-separated): ").split(',')
replacement = input("Enter the replacement word: ")

result = replace_multiple_words(string, words_to_replace, replacement)

print("Original String:", string)
print(f"String after replacing {', '.join(words_to_replace)} with {replacement}:", result)

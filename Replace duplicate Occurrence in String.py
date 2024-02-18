def replace_duplicate_occurrence(s):
    char_count = {}
    result = ''
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
            result += f'[{char}{char_count[char]}]'
        else:
            char_count[char] = 1
            result += char
    
    return result

string = input("Enter a string: ")

result = replace_duplicate_occurrence(string)
print("Original String:", string)
print("String after replacing duplicate occurrences:", result)

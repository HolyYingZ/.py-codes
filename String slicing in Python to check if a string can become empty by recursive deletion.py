def can_become_empty(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return not s
string = input("Enter a string: ")
if can_become_empty(string):
    print(f"The string '{string}' can become empty by recursive deletion.")
else:
    print(f"The string '{string}' cannot become empty by recursive deletion.")

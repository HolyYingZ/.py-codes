import re
def contains_url(s):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    return bool(url_pattern.search(s))

string = input("Enter a string: ")

if contains_url(string):
    print(f"The string '{string}' contains a URL.")
else:
    print(f"The string '{string}' does not contain a URL.")

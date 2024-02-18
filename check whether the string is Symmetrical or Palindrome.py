def is_symmetrical(s):
    return s == s[::-1]
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return is_symmetrical(s)

string = input("Enter a string: ")

if is_palindrome(string):
    print(f"{string} is a palindrome and symmetrical.")
else:
    print(f"{string} is not a palindrome or not symmetrical.")


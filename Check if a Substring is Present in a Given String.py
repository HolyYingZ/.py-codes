def is_substring_present(main_string, substring):
    return substring in main_string

main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")
if is_substring_present(main_string, substring):
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")

def snake_case_to_pascal_case(s):
    words = s.split('_')
    pascal_case = ''.join(word.capitalize() for word in words)
    return pascal_case

# Input string in snake_case
snake_case_string = input("Enter a string in snake_case: ")

# Convert to Pascal case
pascal_case_result = snake_case_to_pascal_case(snake_case_string)

# Display the result
print(f"Original String (snake_case): {snake_case_string}")
print(f"Converted String (Pascal case): {pascal_case_result}")

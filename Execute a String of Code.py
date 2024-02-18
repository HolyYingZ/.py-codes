
code_to_execute = input("Enter a string of Python code to execute: ")

try:
    exec(code_to_execute)
except Exception as e:
    print(f"Error occurred while executing the code: {e}")

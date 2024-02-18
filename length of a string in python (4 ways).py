# Method 1: Using len() function
string = input("Enter a string: ")
length1 = len(string)
print(f"Length using len(): {length1}")

# Method 2: Using loop
length2 = 0
for char in string:
    length2 += 1
print(f"Length using loop: {length2}")

# Method 3: Using count of characters
length3 = sum(1 for char in string)
print(f"Length using count of characters: {length3}")

# Method 4: Using list comprehension
length4 = sum(1 for _ in string)
print(f"Length using list comprehension: {length4}")

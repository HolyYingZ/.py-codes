input_string = "pqrsvwbd"
mirror_dict = {'p': 'q', 'q': 'p', 'b': 'd', 'd': 'b', 'v': 'w', 'w': 'v'}
mirror_characters = [mirror_dict[char] for char in input_string if char in mirror_dict]

print("Original String:", input_string)
print("Mirror Characters:", mirror_characters)

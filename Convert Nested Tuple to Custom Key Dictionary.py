nested_tuple = ((1, 'a'), (2, 'b'), (3, 'c'))
custom_key_dict = {str(tup[0]): tup[1] for tup in nested_tuple}
print("Original Nested Tuple:", nested_tuple)
print("Converted Custom Key Dictionary:", custom_key_dict)

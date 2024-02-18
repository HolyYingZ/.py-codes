from collections import OrderedDict
input_string = "programming"
non_repeating_chars = [char for char, count in OrderedDict.fromkeys(input_string).items() if count == 1]
print("Original String:", input_string)
print("K'th Non-repeating Character:", non_repeating_chars)

from collections import OrderedDict
input_string = "pythonprogramming"

ordered_dict = OrderedDict.fromkeys(input_string)

print("Original String:", input_string)
print("Order of characters in the String:", ''.join(ordered_dict))

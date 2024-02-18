tuple_list = [(12, 'abc', 45), (67, 'def', 89), (123, 'ghi', 456)]
digit_list = [int(''.join(filter(str.isdigit, str(item)))) for tup in tuple_list for item in tup]
print("Original Tuple List:", tuple_list)
print("Extracted Digits List:", digit_list)

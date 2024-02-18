from collections import Counter
str1 = "aabbcc"
str2 = "bcabca"
count_str1 = Counter(str1)
count_str2 = Counter(str2)
intersection_counter = count_str1 & count_str2
result_string = ''.join(intersection_counter.elements())
print("Original Strings:")
print("String 1:", str1)
print("String 2:", str2)
print("Result String using deletion and rearrangement:", result_string)

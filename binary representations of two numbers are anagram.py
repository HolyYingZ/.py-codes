num1 = 8
num2 = 4
binary1 = bin(num1)[2:]
binary2 = bin(num2)[2:]
is_anagram = sorted(binary1) == sorted(binary2)
print("Binary Representation of", num1, ":", binary1)
print("Binary Representation of", num2, ":", binary2)
print("Are Binary Representations Anagrams?", is_anagram)

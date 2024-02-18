#Using the reverse() method
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print("Reversed list:", my_list)

#Using the [::-1] slicing technique
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)

#Using the reversed() function:
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print("Reversed list:", reversed_list)

#Using a loop to create a reversed copy:
my_list = [1, 2, 3, 4, 5]
reversed_list = []
for item in my_list:
    reversed_list.insert(0, item)
print("Reversed list:", reversed_list)
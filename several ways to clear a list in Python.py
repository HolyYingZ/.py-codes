#Using the clear() method
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print("List after clearing:", my_list)

#Assigning an empty list
my_list = [1, 2, 3, 4, 5]
my_list = []
print("List after clearing:", my_list)

#Using slicing
my_list = [1, 2, 3, 4, 5]
my_list[:] = []
print("List after clearing:", my_list)

#Using the del statement
my_list = [1, 2, 3, 4, 5]
del my_list[:]
print("List after clearing:", my_list)

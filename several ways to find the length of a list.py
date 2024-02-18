#Using the len() function
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print("Length of the list:", length)

#Using a loop
my_list = [1, 2, 3, 4, 5]
count = 0
for _ in my_list:
    count += 1
print("Length of the list:", count)

#Using the count() method
my_list = [1, 2, 3, 4, 5]
length = my_list.count(None)  # Counting occurrences of a placeholder (None)
print("Length of the list:", length)

#Using enumerate() and a loop:
my_list = [1, 2, 3, 4, 5]
count = 0
for _, _ in enumerate(my_list):
    count += 1
print("Length of the list:", count)

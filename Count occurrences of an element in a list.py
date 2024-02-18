#Method 1: Using count() method
my_list = [1, 2, 3, 4, 1, 2, 1, 5]
element_to_count = 1
occurrences_count = my_list.count(element_to_count)
print(f"The element {element_to_count} occurs {occurrences_count} times in the list.")

#Method 2: Using collections.Counter
from collections import Counter
my_list = [1, 2, 3, 4, 1, 2, 1, 5]
element_to_count = 1
occurrences_count = Counter(my_list)[element_to_count]
print(f"The element {element_to_count} occurs {occurrences_count} times in the list.")

#Method 3: Using a loop
my_list = [1, 2, 3, 4, 1, 2, 1, 5]
element_to_count = 1
occurrences_count = sum(1 for num in my_list if num == element_to_count)

# Display the count
print(f"The element {element_to_count} occurs {occurrences_count} times in the list.")
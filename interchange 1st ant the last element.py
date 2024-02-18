def interchange_first_and_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]

my_list = list(map(int, input("Enter the elements of the list : ").split()))

interchange_first_and_last(my_list)

print("List after interchanging first and last elements:", my_list)
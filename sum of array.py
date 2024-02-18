def sum_of_array(arr):
    total = 0
    for element in arr:
        total += element
    return total
arr = list(map(int, input("Enter the elements of the array: ").split()))
result = sum_of_array(arr)
print(f"The sum of the array is:", result)
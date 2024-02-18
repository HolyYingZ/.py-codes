def find_largest_element(arr):
    if not arr:
        return "Array is empty."

    largest_element = arr[0]

   
    for element in arr:
        if element > largest_element:
            largest_element = element

    return largest_element

array = [12, 45, 78, 23, 56, 89, 34]

result = find_largest_element(array)

# Display the result
print("Array:", array)
print("Largest Element:", result)

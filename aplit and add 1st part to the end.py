def split_and_rotate_array(arr, split_index):
    if 0 < split_index < len(arr):
        rotated_array = arr[split_index:] + arr[:split_index]
        return rotated_array
    else:
        return "Invalid split index."


array_to_split = [1, 2, 3, 4, 5]


split_index = int(input("Enter the split index: "))

result_array = split_and_rotate_array(array_to_split, split_index)

print("Original Array:", array_to_split)
print(f"Array after splitting at index {split_index} and adding the first part to the end:", result_array)

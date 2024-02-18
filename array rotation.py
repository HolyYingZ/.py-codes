def left_rotate_array(arr, rotation_count):
    n = len(arr)

    rotated_array = arr[rotation_count % n:] + arr[:rotation_count % n]

    return rotated_array

array = [1, 2, 3, 4, 5]

rotation_count = int(input("Enter the number of rotations: "))

rotated_result = left_rotate_array(array, rotation_count)

print("Original Array:", array)
print(f"Array after {rotation_count} left rotations:", rotated_result)

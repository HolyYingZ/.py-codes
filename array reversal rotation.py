def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate_array(arr, rotation_count):
    n = len(arr)

    reverse_array(arr, 0, rotation_count - 1)
    reverse_array(arr, rotation_count, n - 1)
    reverse_array(arr, 0, n - 1)

    return arr


array = [1, 2, 3, 4, 5]

rotation_count = int(input("Enter the number of rotations: "))

rotated_result = left_rotate_array(array, rotation_count)

print("Original Array:", array)
print(f"Array after {rotation_count} left rotations using reversal algorithm:", rotated_result)

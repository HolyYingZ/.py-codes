def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing
arr = list(map(int, input("Enter the elements of the array : ").split()))
if is_monotonic(arr):
    print("The given array is monotonic.")
else:
    print("The given array is not monotonic.")
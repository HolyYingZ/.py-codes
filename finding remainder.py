def find_remainder_of_array_multiplication(arr, n):
    product = 1
    for num in arr:
        product *= num

    remainder = product % n
    return remainder

array_for_remainder = [1, 2, 3, 4, 5]

divisor = int(input("Enter the divisor (n): "))

remainder_result = find_remainder_of_array_multiplication(array_for_remainder, divisor)

print("Array:", array_for_remainder)
print(f"Remainder of array multiplication divided by {divisor}: {remainder_result}")

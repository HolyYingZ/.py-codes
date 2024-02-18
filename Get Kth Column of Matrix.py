def get_kth_column(matrix, k):
    result = [row[k] for row in matrix]
    return result

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

k = int(input("Enter the value of k (column index): "))

result_column = get_kth_column(matrix, k)

print("Original Matrix:")
for row in matrix:
    print(row)

print(f"\nKth Column ({k}th column) of the Matrix:")
print(result_column)

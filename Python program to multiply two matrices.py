def multiply_matrices(matrix1, matrix2):
    result = [[sum(a * b for a, b in zip(row1, col2)) for col2 in zip(*matrix2)] for row1 in matrix1]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result_matrix = multiply_matrices(matrix1, matrix2)

print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nProduct of Matrices:")
for row in result_matrix:
    print(row)

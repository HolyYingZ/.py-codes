def add_matrices(matrix1, matrix2):
    result_add = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result_add

def subtract_matrices(matrix1, matrix2):
    result_sub = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result_sub

# Input matrices
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_add_matrix = add_matrices(matrix1, matrix2)
result_sub_matrix = subtract_matrices(matrix1, matrix2)

print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nSum of Matrices:")
for row in result_add_matrix:
    print(row)

print("\nDifference of Matrices:")
for row in result_sub_matrix:
    print(row)

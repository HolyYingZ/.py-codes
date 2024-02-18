def matrix_product(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Matrices cannot be multiplied. Number of columns in the first matrix should be equal to the number of rows in the second matrix."
    
    result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

   
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

product_result = matrix_product(matrix1, matrix2)

print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nMatrix Product:")
for row in product_result:
    print(row)

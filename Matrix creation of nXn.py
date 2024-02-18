def create_matrix(n):
    result = [[i * n + j + 1 for j in range(n)] for i in range(n)]
    return result
n = int(input("Enter the value of n: "))

result_matrix = create_matrix(n)

print(f"{n}x{n} Matrix:")
for row in result_matrix:
    print(row)

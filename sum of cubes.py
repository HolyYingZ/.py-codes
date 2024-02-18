def sum_of_cubes(a):
    return (a * (a + 1) // 2) ** 2
a = int(input("Enter the value of n: "))
result = sum_of_cubes(a)
print(f"The sum of cubes of the first {a} natural numbers is: ",result)
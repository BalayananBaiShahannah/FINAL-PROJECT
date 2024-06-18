input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sum_of_diagonal = 0

for i in range(len(input_matrix)):
    sum_of_diagonal += input_matrix[i][i]

print("Original Matrix:")
for row in input_matrix:
    print(row)

print("\nSum of diagonal elements:", sum_of_diagonal)

import numpy as np

input_matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

sum_of_rows = np.sum(input_matrix, axis=1)
sum_of_columns = np.sum(input_matrix, axis=0)

print("Original Matrix:")
print(input_matrix)

print("\nSum of rows:")
print(sum_of_rows)

print("\nSum of columns:")
print(sum_of_columns)

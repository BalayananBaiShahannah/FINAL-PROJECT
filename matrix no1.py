def transpose_matrix(matrix):
  
    rows = len(matrix)
    cols = len(matrix[0])  
    
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose

input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

output_matrix = transpose_matrix(input_matrix)

print("Original Matrix:")
for row in input_matrix:
    print(row)

print("\nTransposed Matrix:")
for row in output_matrix:
    print(row)

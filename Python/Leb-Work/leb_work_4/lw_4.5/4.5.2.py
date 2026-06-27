#2. Write a program to transpose a 2D array. Input a $2 \times 3$ matrix and display its transpose
#($3 \times 2$ matrix).

# Input a 2x3 matrix (2 rows, 3 columns)
matrix = []
print("Enter elements for a 2x3 matrix:")
for i in range(2):
    row = []
    for j in range(3):
        row.append(int(input(f"Matrix [{i}][{j}]: ")))
    matrix.append(row)

# Initialize an empty 3x2 matrix for the transpose
transpose = [[0, 0], [0, 0], [0, 0]]

# Computing transpose: swap rows and columns
for i in range(2):
    for j in range(3):
        transpose[j][i] = matrix[i][j]

print("\nOriginal 2x3 Matrix:")
for row in matrix:
    print(row)

print("\nTransposed 3x2 Matrix:")
for row in transpose:
    print(row)

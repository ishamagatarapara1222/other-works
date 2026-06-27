#1. Implement a program to create a 2D array (list of lists) representing a $3 \times 3$ matrix. Display the matrix in a
#tabular format.

# Creating a 3x3 matrix via user input
matrix = []
print("Enter elements for a 3x3 matrix:")

for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Enter element at [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

# Displaying the matrix in tabular format
print("\nThe 3x3 Matrix is:")
for row in matrix:
    for element in row:
        print(element, end="\t")  # Use tab space for alignment
    print()  # Newline after each row

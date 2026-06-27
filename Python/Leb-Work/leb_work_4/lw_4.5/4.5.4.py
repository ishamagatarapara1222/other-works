#4. Write a program to find the maximum and minimum values in a 2D array.

# Sample 2D array
matrix = [
    [45, 12, 89],
    [34, 7, 66],
    [91, 23, 50]
]

# Initialize max and min with the very first element of the array
max_val = matrix[0][0]
min_val = matrix[0][0]

# Loop through every element to track global max and min
for row in matrix:
    for element in row:
        if element > max_val:
            max_val = element
        if element < min_val:
            min_val = element

print("Matrix:")
for row in matrix:
    print(row)

print(f"\nMaximum Value: {max_val}")
print(f"Minimum Value: {min_val}")

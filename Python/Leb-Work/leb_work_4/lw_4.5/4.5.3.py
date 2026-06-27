#3. Develop a program to calculate the sum of all elements in a 2D array separately.

# Sample 2D array
matrix = [
    [5, 10, 15],
    [20, 25, 30]
]

total_sum = 0

# Iterating through rows and columns to accumulate the sum
for row in matrix:
    for element in row:
        total_sum += element

print("Matrix:")
for row in matrix:
    print(row)

print(f"\nSum of all elements in the 2D array: {total_sum}")

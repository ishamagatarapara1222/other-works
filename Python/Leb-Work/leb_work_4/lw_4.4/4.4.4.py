#4. Create an array of numbers from 1 to 10. Multiply each element by 2 and print the result.

# Creating an array of numbers from 1 to 10
numbers = list(range(1, 11))

print("Original Array:", numbers)
print("Result after multiplying each element by 2:")

# Multiplying and printing
for num in numbers:
    print(num * 2, end=" ")
print()  # For a new line at the end

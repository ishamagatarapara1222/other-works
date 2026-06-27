#1. Write a program to find the length of a 1D array without using any built-in function (like len()).

# Taking user input for array size
size = int(input("Enter array size: "))
array = []

print("Enter array elements:")
for i in range(size):
    element = int(input(f"a[{i}] = "))
    array.append(element)

# Finding length without built-in functions
count = 0
for item in array:
    count += 1

print("\nOutput:")
print(f"Length of an Array: {count}")

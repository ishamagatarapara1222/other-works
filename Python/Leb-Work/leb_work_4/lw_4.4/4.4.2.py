#2. Write a program to find the average of a 1D array without using any built-in function (like sum() or len()).

# Taking user input for array size
size = int(input("Enter array size: "))
array = []

print("Enter array elements:")
for i in range(size):
    element = int(input(f"a[{i}] = "))
    array.append(element)

# Calculating sum and count manually
total_sum = 0
count = 0
for num in array:
    total_sum += num
    count += 1

# Calculating average
average = total_sum / count

print("\nOutput:")
print(f"Average of an Array: {average:.1f}")

#3. Write a program to perform the addition operation of two 1D arrays & store it in another array. Keep in mind that
#both array sizes must be the same.

# Taking user input for array size
size = int(input("Enter array size: "))

array_A = []
print("\nEnter array A's elements:")
for i in range(size):
    element = int(input(f"a[{i}] = "))
    array_A.append(element)

array_B = []
print("\nEnter array B's elements:")
for i in range(size):
    element = int(input(f"b[{i}] = "))
    array_B.append(element)

# Element-wise addition into Array C
array_C = []
for i in range(size):
    array_C.append(array_A[i] + array_B[i])

print("\nOutput:")
# Formatting the output list as a clean, comma-separated string
print("Array C is:", ", ".join(map(str, array_C)))

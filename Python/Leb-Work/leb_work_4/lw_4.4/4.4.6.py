'''
6. In a user-defined array (by taking input):

Print all even numbers from the array.

Print all odd numbers from the array.
'''

# Creating user-defined array
size = int(input("Enter the number of elements: "))
array = []

print("Enter array elements:")
for i in range(size):
    array.append(int(input(f"Element {i+1}: ")))

# Finding and printing even numbers
print("\nEven numbers from the array:")
for num in array:
    if num % 2 == 0:
        print(num, end=" ")
print()

# Finding and printing odd numbers
print("Odd numbers from the array:")
for num in array:
    if num % 2 != 0:
        print(num, end=" ")
print()


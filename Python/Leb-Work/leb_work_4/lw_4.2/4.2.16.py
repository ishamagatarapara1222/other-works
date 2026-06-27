#4.2.16
#Implement a program to create a function that returns a tuple containing the square and cube of a given number.

def square_cube(num):
    return num ** 2, num ** 3

square, cube = square_cube(5)

print("Square =", square)
print("Cube =", cube)

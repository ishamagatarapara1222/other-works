#4.1.5
#Create a program that takes a user-defined function as an argument to calculate the cube of a list of numbers

def cube(x):
    return x ** 3

def apply_function(func, numbers):
    return [func(num) for num in numbers]

nums = [1, 2, 3, 4]
print(apply_function(cube, nums))

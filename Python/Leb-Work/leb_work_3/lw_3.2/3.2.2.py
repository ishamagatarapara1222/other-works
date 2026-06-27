#3.2.2
'''
Create a tuple of 5 numbers.

Access the third item.
Try to change the second value and observe the result.
'''
numbers = (10, 20, 30, 40, 50)

print("Third item:", numbers[2])

# Tuples cannot be changed
try:
    numbers[1] = 25
except TypeError:
    print("Error: Tuple values cannot be changed")

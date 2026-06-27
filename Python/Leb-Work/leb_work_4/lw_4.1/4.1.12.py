#4.1.12
'''
Create a function that calculates the area of a rectangle.

Add a doc string to describe the function's purpose, parameters, and return type.
Write code to print the doc string.
'''

def rectangle_area(length, width):
    """
    Calculate area of rectangle.

    Parameters:
    length - length of rectangle
    width - width of rectangle

    Returns:
    Area of rectangle
    """
    return length * width

print("Area =", rectangle_area(5, 4))

print("\nDoc String:")
print(rectangle_area.__doc__)

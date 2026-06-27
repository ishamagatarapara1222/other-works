#4.2.15
#Develop a function that calculates the area and perimeter of a rectangle and returns both values.

def rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)

    return area, perimeter

a, p = rectangle(5, 4)

print("Area =", a)
print("Perimeter =", p)

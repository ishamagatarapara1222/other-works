#Create a base class Shape and override its area() method in Circle and Rectangle.

import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

# Testing polymorphism
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area():.2f}")

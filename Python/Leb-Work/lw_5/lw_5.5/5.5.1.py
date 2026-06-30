'''
1. Create an abstract class Shape with an abstract method area().

Inherit two child classes Rectangle and Circle, each implementing the area() method.

Demonstrate that creating an object of Shape directly raises an error.

Compute and display area for both Rectangle and Circle.
'''

from abc import ABC, abstractmethod
import math

# 1. Create an abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# 2. Inherit child classes implementing area()
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)

# --- Demonstration & Execution ---

# Demonstrate that instantiating Shape directly raises an error
try:
    print("Attempting to create an instance of Shape...")
    shape = Shape()
except TypeError as e:
    print(f"Error caught successfully: {e}\n")

# Compute and display area for Rectangle and Circle
rect = Rectangle(5, 10)
circ = Circle(7)

print(f"Rectangle Area (5x10): {rect.area()}")
print(f"Circle Area (radius 7): {circ.area():.2f}")

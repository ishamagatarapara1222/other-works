'''
2.
Add another abstract method perimeter() in the Shape class.

Implement it in Rectangle and Circle subclasses.

Verify both area() and perimeter() work correctly.

Try to instantiate a new subclass without implementing one method — observe the error.
'''

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
        
    # Add perimeter abstract method
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)
        
    def perimeter(self):
        return 2 * math.pi * self.radius

# A broken subclass that forgets to implement perimeter()
class IncompleteShape(Shape):
    def area(self):
        return 100
    # perimeter() is missing!

# --- Demonstration & Execution ---

# Verify working implementation
rect = Rectangle(4, 6)
print(f"Rectangle Area: {rect.area()}, Perimeter: {rect.perimeter()}")

circ = Circle(5)
print(f"Circle Area: {circ.area():.2f}, Perimeter: {circ.perimeter():.2f}\n")

# Try to instantiate the incomplete subclass to observe the error
try:
    print("Attempting to instantiate IncompleteShape...")
    incomplete = IncompleteShape()
except TypeError as e:
    print(f"Error caught successfully: {e}")

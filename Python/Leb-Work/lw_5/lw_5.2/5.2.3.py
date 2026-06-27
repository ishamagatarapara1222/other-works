#3. Write a program to demonstrate a parameterized constructor in the class Rectangle. Initialize the length and
#width using the constructor and calculate the area.

class Rectangle:
    # Parameterized constructor accepting parameters during instantiation
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def display_details(self):
        print(f"Rectangle Dimensions: {self.length} x {self.width}")
        print(f"Calculated Area     : {self.calculate_area()}")

# Instantiating the object with dynamic values
rect = Rectangle(12.5, 4.0)
rect.display_details()

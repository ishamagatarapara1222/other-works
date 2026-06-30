#7. Implement overload logic for calculating circle vs rectangle area by utilizing a @classmethod or @staticmethod.

class AreaCalculator:
    @staticmethod
    def area(shape_type, *args):
        if shape_type.lower() == "circle" and len(args) == 1:
            radius = args[0]
            import math
            return math.pi * (radius ** 2)
        elif shape_type.lower() == "rectangle" and len(args) == 2:
            width, height = args[0], args[1]
            return width * height
        else:
            return "Invalid shape or arguments!"

# Testing static method overloading simulation
print("Area of Circle:", AreaCalculator.area("circle", 7))
print("Area of Rectangle:", AreaCalculator.area("rectangle", 5, 10))

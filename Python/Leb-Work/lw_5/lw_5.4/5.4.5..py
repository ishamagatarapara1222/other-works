#5. Create a Calculator class with a multiply() method that handles 2 or 3 arguments using default values.class Calculator:

class Calculator:

    def multiply(self, a, b, c=None):
        if c is not None:
            return a * b * c
        return a * b

# Testing
calc = Calculator()
print("Multiplication of 2 numbers (4 * 5):", calc.multiply(4, 5))
print("Multiplication of 3 numbers (4 * 5 * 2):", calc.multiply(4, 5, 2))

try:
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    print("Result:", num1 / num2)
except ValueError:
    print("Error: Please enter numbers only!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    # Runs regardless of what happened above
    print("Division attempt finished.")
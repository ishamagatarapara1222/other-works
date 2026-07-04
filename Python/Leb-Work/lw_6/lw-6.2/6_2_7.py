import math

try:
    number = float(input("Enter a number: "))
    if number < 0:
        # Negative numbers don't have a real square root, so we raise an error
        raise ValueError("Negative numbers are not allowed.")
    
    square_root = math.sqrt(number)
except ValueError as error:
    print("Error:", error)
else:
    # Runs only if the number was valid and positive
    print(f"The square root is: {square_root}")
finally:
    # Runs at the very end no matter what
    print("Execution complete.")
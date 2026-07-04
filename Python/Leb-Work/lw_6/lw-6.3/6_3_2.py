def check_even(num):
    # Check if the type is exactly an integer
    if not isinstance(num, int):
        raise TypeError("Input must be a whole integer!")
    
    # Check if the number is odd
    if num % 2 != 0:
        raise ValueError("The number is odd!")
    
    print(f"{num} is a valid even number.")

# Testing the function
try:
    check_even(4)        # Valid
    # check_even(3)      # Will raise ValueError
    # check_even("abc")  # Will raise TypeError
except (TypeError, ValueError) as e:
    print("Error:", e)
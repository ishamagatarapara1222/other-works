#9. Write a program to retrieve the documentation string of a class or function using the help() function.

def calculate_square(n):
    """
    This function takes a number n and returns its square.
    It is used to demonstrate docstrings.
    """
    return n * n

# Using help() to view the documentation
print("--- Output of help(calculate_square) ---")
help(calculate_square)

#4.1.13
'''
Develop a program that uses a UDF to return the Fibonacci sequence up to a given number.

Include a detailed doc string explaining the function's working, input, and output.
'''

def fibonacci(n):
    """
    Generate Fibonacci sequence up to a given number.

    Input:
    n - maximum number in sequence

    Output:
    Returns a list containing Fibonacci numbers
    up to the given limit.
    """

    a = 0
    b = 1
    result = []

    while a <= n:
        result.append(a)
        a, b = b, a + b

    return result

num = int(input("Enter limit: "))
print(fibonacci(num))

print("\nDoc String:")
print(fibonacci.__doc__)

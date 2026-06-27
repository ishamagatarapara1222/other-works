#4.2.2
'''
Implement a recursive function to calculate the nth Fibonacci number.

Test the function with various inputs.
'''

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter n: "))
print(fibonacci(num))

#4.2.1
'''
Write a recursive function to calculate the factorial of a given number.

Ensure the program handles edge cases (e.g., negative inputs)
'''

def factorial(n):
    if n < 0:
        return "Negative number not allowed"

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

num = int(input("Enter number: "))
print(factorial(num))

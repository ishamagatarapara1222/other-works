'''
Q.3
Implement a program that:

Takes three integers as input.
Uses an if-elif-else statement to find and print the largest number
'''
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a>b and a>c:
    print("Largest number is:",a)
elif b>a and b>c:
    print("Largest number is:",b)
else:
    print("Largest number is:",c)


#lw_2.2
'''
Q.1
Write a Program in Python to find the maximum number from the given three numbers using a nested if statement
'''

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a>b:
    if a>c:
        print("Maximum number is:",a)
    else:
        print("Maximum number is:",c)
else:
    if b>c:
        print("Maximum number is:",b)
    else:
        print("Maximum number is:",c)

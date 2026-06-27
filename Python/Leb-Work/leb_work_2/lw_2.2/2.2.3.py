'''
Q.3
Write a Program in Python to find the maximum number from the given four numbers using a nested if statement.
'''
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))

if a>b:
    if a>c:
        if a>d:
            print("Maximum number is:",a)
        else:
            print("Maximum number is:",d)
    else:
        if c>d:
            print("Maximum number is:",c)
        else:
            print("Maximum number is:",d)
else:
    if b>c:
        if b>d:
            print("Maximum number is:",b)
        else:
            print("Maximum number is:",d)
    else:
        if c>d:
            print("Maximum number is:",c)
        else:
            print("Maximum number is:",d)

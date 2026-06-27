'''
Q.2
Write a Program in Python to find the minimum number from the given three numbers using a nested if statement.
'''
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a<b:
    if a<c:
        print("Minimun number is:",a)
    else:
        print("Minimum number is:",c)
else:
    if b<c:
        print("Minimum number is:",b)
    else:
        print("Minimum number is:",c)

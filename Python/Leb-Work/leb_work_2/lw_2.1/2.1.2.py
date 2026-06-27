'''
Q.2
Create a program that:

Accepts a user's age as input.
Uses nested if-else statements to categorize the user into age groups:
Child (0–12)
Teenager (13–19)
Adult (20–59)
Senior (60+)
'''

age = int(input("Enter your age:"))

if age >= 0:
    if age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 59:
        print("Adult")
    else:
        print("Senior")
else:
    print("Invalid input")
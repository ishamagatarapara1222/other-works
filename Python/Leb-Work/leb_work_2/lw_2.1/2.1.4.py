'''
Q.4
Write a Python program to:

Take a number as input from the user and check whether it is a neutral number or not using a ladder if statement
'''
a = int(input("Enter a number:"))

if a > 0:
    print("Positive number.")
elif a < 0:
    print("Negative number.")
else:
    print("Neutral number.")


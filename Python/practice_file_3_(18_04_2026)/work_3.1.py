#3.1 :  Check greater number between two inputs

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both numbers are equal")

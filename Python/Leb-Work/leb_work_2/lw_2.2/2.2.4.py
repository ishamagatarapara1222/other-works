'''
Q.4
Write a Python program using a switch-case equivalent to:

Take an operator (+, -, *, /) as input.
Perform the corresponding operation on two numbers entered by the user.
'''
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

op = input("Enter operator (+,-,*,/):")

match op:
    case "+":
        print("Addition =",num1+num2)
    case "-":
        print("Substraction =", num1-num2)
    case "*":
        print("Multiplication =",num1*num2)
    case "/":
        if num2 != 0:
            print("Division =", num1/num2)
        else:
            print("Can not divide by zero(0).")
    case _:
        print("Invalid input")
    

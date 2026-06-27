#7.5 : Mini calculator with all operators

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
op = input("Enter opertor (+,-,*,/):")

if op == '+':
    print("Addision = ", num1+num)
elif op == '-':
    print("Substraction =", num1-num2)
elif op == '*':
    print("Multiplication =", num1*num2)
elif op == '/':
    if num != 0:
        print("Division =", num1/num2)
    else :
        print("Error! Number can not divided by zero.")
else:
    print("Invalid input")

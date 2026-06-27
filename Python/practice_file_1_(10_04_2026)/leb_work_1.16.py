#Q16. Find the largest of three numbers using comparison operators. [Medium]

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a >= b  and  a >= c:
    print("Largest =", a)
elif b >= c  and b >= a:
    print("Largest =", b)
else :
    print("Largest = ", c)
    

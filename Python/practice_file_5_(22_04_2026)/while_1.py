#while_1. Sum of digits

num = int(input("Enter a number: "))

total = 0

while num>0:
    digit = num %10
    total += digit
    num = num // 10

print("Sum of digit", total)





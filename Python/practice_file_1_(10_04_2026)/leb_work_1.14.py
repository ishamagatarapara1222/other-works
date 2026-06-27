#Q14. Find the sum of digits of a 3-digit number using // and % operators. [Hard]

num = int(input("Enter a 3-digit Number"))

a = num // 100
b = (num // 10) % 10
c = num % 10

sum_digits = a+b+c

print("Sum of digit = ", sum_digits)

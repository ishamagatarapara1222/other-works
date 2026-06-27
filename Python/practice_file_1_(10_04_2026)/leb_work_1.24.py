#Q24. Use the bitwise AND (&) operator to check if a number is even or odd. [Hard]

num = int(input("Enter a number: "))

if num & 1:
    print("Odd")
else:
    print("Even")

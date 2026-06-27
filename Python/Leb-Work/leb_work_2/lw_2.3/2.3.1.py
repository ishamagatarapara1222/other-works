#lw_2.3.1  Take numbers until user enters 0

num = int(input("Enter a number (0 to stop): "))

while num != 0:
    print("You entered:", num)
    num = int(input("Enter a number (0 to stop): "))

print("Program Ended")


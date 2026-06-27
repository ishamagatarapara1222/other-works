#1.9 Check leap year

year = int(input("Enter year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a Leap year...!")
else:
    print("Its not leap year...!")

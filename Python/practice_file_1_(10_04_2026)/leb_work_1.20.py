#Q20. Check if a user's age is >= 18 OR they are a student using or operator. [Medium]

age = int(input("Enter your age:"))
student = input("Are you a student? (yes/no): ")

if age >= 18 or student.lower()=="yes":
    print("Condition is satisfied.")
else:
    print("Condition is not satisfied.")

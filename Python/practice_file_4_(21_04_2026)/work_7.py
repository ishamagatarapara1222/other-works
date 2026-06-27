#7. Take user age as string and:
# convert to int
# check if eligible to vote

age_text = input("Enter your age:")
age = int(age_text)

if age>=18:
    print("You are eligible to voting....!")
elif age<18 and age>=0:
    print("You are not eligible to voting....!")
else:
    print("Invalid input")

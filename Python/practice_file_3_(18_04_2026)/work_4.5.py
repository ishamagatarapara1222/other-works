#4.5 :  Validate input (age > 18 AND city == "Surat")

age = int(input("Enter your age: "))
city = input("Enter your city: ")

if age > 18 and city.lower() == "surat":
    print("Valid input")
else:
    print("Invalid input")

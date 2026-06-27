#1.10 Menu driven calculator

while True:
    print("\n--- MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Calculator band ho raha hai...")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", a + b)

    elif choice == 2:
        print("Result =", a - b)

    elif choice == 3:
        print("Result =", a * b)

    elif choice == 4:
        if b != 0:
            print("Result =", a / b)
        else:
            print("Error: Division by zero!")

    else:
        print("Invalid choice! Try again.")

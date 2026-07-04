try:
    number = int(input("Enter a number: "))
    if number < 0:
        # raise manually triggers an error
        raise ValueError("Negative numbers are not allowed!")
    print("You entered:", number)
except ValueError as e:
    print("Caught an error:", e)
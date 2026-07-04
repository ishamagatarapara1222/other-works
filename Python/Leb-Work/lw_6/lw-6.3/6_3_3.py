try:
    age = int(input("Enter your age: "))
    # assert checks if a condition is True. If False, it throws an AssertionError
    assert age > 18, "Age must be above 18!"
    print("Access granted.")
except AssertionError as e:
    print("Assertion Error:", e)
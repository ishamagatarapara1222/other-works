def check_palindrome(s):
    # Ensure the string is not empty or just spaces
    assert len(s.strip()) > 0, "String cannot be empty!"
    
    # Check if string reads the same backwards
    if s == s[::-1]:
        print(f"'{s}' is a palindrome!")
    else:
        print(f"'{s}' is not a palindrome.")

# Testing the function
try:
    check_palindrome("radar")
    check_palindrome("")  # This will trigger the assertion error
except AssertionError as e:
    print("Error:", e)
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    # Check if '@' is in the email and if it ends with .com or .org
    if "@" not in email or not (email.endswith(".com") or email.endswith(".org")):
        raise InvalidEmailError("Invalid format! Email must contain '@' and end with .com or .org")
    
    print(f"'{email}' is a valid email address.")

# Testing
try:
    user_email = input("Enter your email: ")
    validate_email(user_email)
except InvalidEmailError as e:
    print("Validation Error:", e)
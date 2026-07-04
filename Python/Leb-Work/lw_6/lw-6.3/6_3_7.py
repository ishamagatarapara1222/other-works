class InvalidGradeError(Exception):
    pass

try:
    user_input = input("Enter student grade: ")
    
    # Assert that the input is not empty
    assert user_input.strip() != "", "Grade input cannot be blank!"
    
    grade = float(user_input)
    
    # Check if the grade is between 0 and 100
    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100.")
        
    # Check if the grade is below 40
    if grade < 40:
        raise InvalidGradeError("Failing grade! Score is below 40.")
        
    print(f"Grade of {grade} is valid and passing!")

except AssertionError as ae:
    print("Input Error:", ae)
except ValueError as ve:
    print("Range Error:", ve)
except InvalidGradeError as ige:
    print("Grade Status Error:", ige)
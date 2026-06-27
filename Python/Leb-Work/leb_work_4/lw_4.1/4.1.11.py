#4.1.11
'''
Develop a program that allows users to pass any combination of attributes for an employee (e.g., name, department, salary) using **kwargs.

Check if any required fields are missing and print a message accordingly
'''

def employee_info(**kwargs):
    required = ["name", "department", "salary"]

    for field in required:
        if field not in kwargs:
            print(field, "is missing")
            return

    print("Employee Details")
    for key, value in kwargs.items():
        print(key, ":", value)

employee_info(
    name="Rohan",
    department="IT",
    salary=30000
)

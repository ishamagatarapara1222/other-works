#11. Invoke the parent constructor of Employee containing attributes name and salary from within the Manager
#constructor.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        # Call the parent constructor to initialize name and salary
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Manager: {self.name} | Salary: ${self.salary} | Department: {self.department}")

# Testing
mgr = Manager("Sarah Jenkins", 95000, "AI Development")
mgr.display_info()

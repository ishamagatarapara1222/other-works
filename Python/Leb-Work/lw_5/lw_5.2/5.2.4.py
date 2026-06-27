#4. Create a class Employee with a default constructor to initialize attributes and a destructor to display a
#farewell message when the object is deleted.

class Employee:
    # A default constructor sets pre-defined, uniform fallback values
    def __init__(self):
        self.name = "Guest/New Hire"
        self.department = "General"
        print(f"Default Profile Generated: {self.name} assigned to {self.department}")

    # Destructor to manage a clean sign-off routine
    def __del__(self):
        print(f"Farewell Message: Employee profile for '{self.name}' has closed out successfully.")

print("--- Initializing Employee ---")
emp = Employee()

# Optional: Modifying values later down the execution pipeline
emp.name = "Rohan Sharma"
emp.department = "AI/ML Engineering"
print(f"Updated Profile: {emp.name} is working in {emp.department}.\n")

print("--- Program Execution Ending (Object Scoping Will Clean Up) ---")
# When code blocks terminate or objects are overwritten, the destructor auto-triggers

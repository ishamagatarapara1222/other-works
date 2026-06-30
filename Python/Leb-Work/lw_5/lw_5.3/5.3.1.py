#1. Create a program to demonstrate Single Inheritance where a class Parent has a method display(), and a child class
#Child inherits and calls this method

class Parent:
    def display(self):
        print("This is the display method from the Parent class.")

class Child(Parent):
    pass

# Demonstration
child_obj = Child()
child_obj.display()  # Calling the inherited method

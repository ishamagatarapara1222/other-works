#13. Call a parent base class method display() from within an overridden method in a derived subclass using super().

class Base:
    def display(self):
        print("Base class display functionality executed.")

class Derived(Base):
    def display(self):
        # Call the parent class's display method first
        super().display()
        # Add custom extended functionality
        print("Derived class extended functionality executed.")

# Testing
obj = Derived()
obj.display()

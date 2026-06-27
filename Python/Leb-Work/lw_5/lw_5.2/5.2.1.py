#1. Write a program that creates multiple objects of a class and deletes them using the del keyword. Observe the
#behavior (using the destructor)

class Sample:
    def __init__(self, name):
        self.name = name
        print(f"Object '{self.name}' has been created.")

    # The destructor method gets automatically invoked when an object is destroyed
    def __del__(self):
        print(f"Destructor called: Object '{self.name}' has been deleted.")

# Creating multiple objects
obj1 = Sample("Alpha")
obj2 = Sample("Beta")

print("\n--- Explicitly deleting objects now ---")
del obj1
print("Object 1 manual deletion command finished.\n")

del obj2
print("Object 2 manual deletion command finished.")


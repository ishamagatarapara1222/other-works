#7. Write a program to list all the attributes and methods of a class using the dir() function.

class SampleClass:
    def __init__(self):
        self.value = 10
        
    def custom_method(self):
        pass

# Listing all attributes and methods
print("Attributes and methods of SampleClass:")
print(dir(SampleClass))

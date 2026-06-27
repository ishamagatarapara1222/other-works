#1. Create a class Person with attributes such as name and age.

#Write a method to display the details.

#Create multiple objects and call the method for each.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating multiple objects
person1 = Person("Amit", 19)
person2 = Person("Priya", 21)
person3 = Person("Rahul", 18)

# Calling the method for each object
print("--- Person Details ---")
person1.display_details()
person2.display_details()
person3.display_details()

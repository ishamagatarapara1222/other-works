#6.Override a speak() method from a base Animal class in Dog and Cat subclasses.

class Animal:
    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Testing
animals = [Dog(), Cat()]
for animal in animals:
    print(f"{type(animal).__name__} says: {animal.speak()}")

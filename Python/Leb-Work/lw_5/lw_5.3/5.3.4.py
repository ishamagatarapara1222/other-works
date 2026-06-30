#4. Create a program to demonstrate Hierarchical Inheritance where a base class Animal is inherited by two subclasses
#Dog and Cat, each having their specific methods.

class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal):
    def bark(self):
        print("The dog barks: Woof! Woof!")

class Cat(Animal):
    def meow(self):
        print("The cat meows: Meow! Meow!")

# Demonstration
dog = Dog()
cat = Cat()

dog.eat()   # Shared base method
dog.bark()  # Dog specific

cat.eat()   # Shared base method
cat.meow()  # Cat specific

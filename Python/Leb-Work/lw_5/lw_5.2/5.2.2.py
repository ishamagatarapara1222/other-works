#2. Create a class Animal with a constructor that initializes the name attribute. Add a method to display the name
#of the animal

class Animal:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"The animal's name is: {self.name}")

# Creating an instance of Animal
pet = Animal("Leo the Lion")

# Calling the display method
pet.display_name()

#6.  Develop a program that uses getter and setter methods to validate the age of a person (e.g., age must be greater
#than 0)


class ValidatedPerson:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)  # Route initialization through the setter for safety

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("[Validation Error]: Age must be strictly greater than 0. Setting default age to 1.")
            self.__age = 1

    def get_age(self):
        return self.__age

# Test Case 1: Valid Inputs
p1 = ValidatedPerson("Karan", 20)
print(f"{p1.name} is {p1.get_age()} years old.\n")

# Test Case 2: Invalid Input
p2 = ValidatedPerson("Child", -5)
print(f"{p2.name} is updated to {p2.get_age()} year old.")

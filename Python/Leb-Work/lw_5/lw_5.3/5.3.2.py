#2. Implement a program to demonstrate Multiple Inheritance using classes Teacher and Administrator inherited by a
#class Headmaster.

class Teacher:
    def teach(self):
        print("Teaching students...")

class Administrator:
    def manage(self):
        print("Managing school administration...")

class Headmaster(Teacher, Administrator):
    def role(self):
        print("I am the Headmaster, I can both teach and manage.")

# Demonstration
hm = Headmaster()
hm.teach()   # From Teacher
hm.manage()  # From Administrator
hm.role()    # From Headmaster

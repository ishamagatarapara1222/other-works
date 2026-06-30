#3.  Write a program to demonstrate Multilevel Inheritance using a class hierarchy: Grandparent -> Parent -> Child.
#Each class should have a method to display its role.

class Grandparent:
    def display_grandparent(self):
        print("Role: Grandparent")

class Parent(Grandparent):
    def display_parent(self):
        print("Role: Parent")

class Child(Parent):
    def display_child(self):
        print("Role: Child")

# Demonstration
child_obj = Child()
child_obj.display_grandparent() 
child_obj.display_parent()      
child_obj.display_child()       

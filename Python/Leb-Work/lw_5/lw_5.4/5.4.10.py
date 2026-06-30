#10. Define Person and Student (derived from Person) classes and use issubclass() to verify relationship status.

class Person:
    pass

class Student(Person):
    pass

# Checking relationships
is_child = issubclass(Student, Person)
is_parent = issubclass(Person, Student)

print(f"Is Student a subclass of Person? {is_child}")
print(f"Is Person a subclass of Student? {is_parent}")

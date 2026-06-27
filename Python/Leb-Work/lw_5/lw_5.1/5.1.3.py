#3.  Explain the behavior when self is omitted in a method definition using a small example.
'''
Explanation
In Python, instance methods must accept the current object instance as their first parameter, conventionally named
self. If you omit self from a method definition, Python will treat it like a static function embedded inside the
class block.

When you attempt to call that method using an object instance (e.g., obj.method()), Python automatically injects the
object instance as the first argument behind the scenes. Because the method was defined with zero parameters,
a TypeError is raised stating that the method was given an unexpected argument.
'''
class Dog:
    def __init__(self, name):
        self.name = name

    # Incorrect method definition: 'self' is omitted
    def bark():
        print("Woof Woof!")

# Instantiating the object
my_dog = Dog("Buddy")

print("Attempting to call a method without 'self':")
try:
    my_dog.bark()  # This will cause a crash
except TypeError as error:
    print(f"\n[ERROR CAUGHT] TypeError: {error}")

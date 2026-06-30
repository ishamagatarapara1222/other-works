#8. Develop a program to check if an object is an instance of a particular class using the isinstance() function.

class Vehicle:
    pass

class Car(Vehicle):
    pass

my_car = Car()

# Checking instances
is_car = isinstance(my_car, Car)
is_vehicle = isinstance(my_car, Vehicle)
is_string = isinstance(my_car, str)

print(f"Is 'my_car' an instance of Car? {is_car}")
print(f"Is 'my_car' an instance of Vehicle? {is_vehicle} (True due to inheritance)")
print(f"Is 'my_car' an instance of string (str)? {is_string}")

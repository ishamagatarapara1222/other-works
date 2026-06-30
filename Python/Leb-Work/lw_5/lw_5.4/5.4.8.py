#8.Override a start() method from a parent Vehicle class inside Bike and Car subclasses.
class Vehicle:
    def start(self):
        print("Vehicle engine starts spinning.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts: Kick-start or button-press, engine purrs!")

class Car(Vehicle):
    def start(self):
        print("Car starts: Push button ignition engaged, dashboard lights up!")

# Testing
vehicles = [Bike(), Car()]
for v in vehicles:
    v.start()

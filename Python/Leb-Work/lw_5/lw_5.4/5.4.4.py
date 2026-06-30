#4. Define an abstract concept/interface Transport and implement travel() differently in Train and Plane.

class Transport:
    def travel(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Train(Transport):
    def travel(self):
        return "Traveling on tracks through the countryside."

class Plane(Transport):
    def travel(self):
        return "Flying through the clouds at high altitude."


def start_journey(vehicle: Transport):
    print(vehicle.travel())

# Testing
start_journey(Train())
start_journey(Plane())

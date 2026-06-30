#5. Develop a program to demonstrate Hybrid Inheritance by combining Multilevel and Multiple inheritance. Show how
#the super() function helps resolve ambiguity.


class Device:
    def __init__(self):
        print("Device initialized")

class Computer(Device):
    def __init__(self):
        super().__init__()
        print("Computer features added")

class Camera(Device):
    def __init__(self):
        super().__init__()
        print("Camera features added")


class SmartPhone(Computer, Camera):
    def __init__(self):
     
        super().__init__()
        print("SmartPhone fully initialized")

# Demonstration
phone = SmartPhone()

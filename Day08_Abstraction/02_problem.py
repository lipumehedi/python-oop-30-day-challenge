from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        return "Car engine started"
    
class Motorcycle(Vehicle):
    def start(self):
        return "Motorcycle engine started"
    
class ElectricCar(Vehicle):
    def start(self):
        return "Electric car started silently"
    
    

car1 = Car()
motorcycle1 = Motorcycle()
electric_car1 = ElectricCar()

print(car1.start())
print(motorcycle1.start())
print(electric_car1.start())

vehicles = [car1, motorcycle1, electric_car1]

for vehicle in vehicles:
    print(vehicle.start())
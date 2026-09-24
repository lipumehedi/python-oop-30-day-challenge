class ElectricCar:
    def __init__(self):
        self.battery = Battery()
        
class Battery:
    def charge(self):
        return "Battery charging"
    
car1 = ElectricCar()

print(car1.battery.charge())
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        return f"{self.brand} - {self.speed} km/h"
    

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors
        
    
    def show_car_info(self):
        return f"{self.brand} - {self.speed} km/h - {self.doors} doors"
    
car1 = Car("Toyota", 180, 4)

print(car1.brand)
print(car1.speed)
print(car1.show_info())
print(car1.show_car_info()) 


   

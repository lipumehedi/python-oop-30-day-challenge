class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
car1 = Car("Toyota", "Prius", 2022)
car2 = Car("Honda", "Civic", 2024)


print(car1.brand)
print(car1.model)
print(car1.year)

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
car1 = Car("Toyota", "Prius", 2022)
car2 = Car("Honda", "Civic", 2024)


print("Brand:", car1.brand)
print("Model:",car1.model)
print("Year:",car1.year)
print("\nBrand:", car2.brand)
print("Model:",car2.model)
print("Year:",car2.year)

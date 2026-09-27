class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __eq__(self, other):
        return self.price == other.price
    
product1 = Product("Laptop", 80000)
product2 = Product("Desktop", 80000)
product3 = Product("Mouse", 1500)

print(product1 == product2)  
print(product1 == product3)  
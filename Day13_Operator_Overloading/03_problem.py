class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
        
    def __mul__(self, other):
       return self.price * self.quantity * other.price * other.quantity
    
product1 = Product(100, 3)
product2 = Product(50, 2)

print(product1 * product2)
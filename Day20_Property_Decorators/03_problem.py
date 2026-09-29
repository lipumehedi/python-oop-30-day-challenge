class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")

        self._price = value

product = Product(1000)

print(product.price)

product.price = 1500
print(product.price)
product.price = -500
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
    
    
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
        
circle1 = Circle(5)
rectangle1 = Rectangle(10, 5)
triangle1 = Triangle(10, 6)

print(circle1.area())
print(rectangle1.area())
print(triangle1.area())
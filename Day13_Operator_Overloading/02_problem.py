class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __sub__(self, other):
       return Point(self.x - other.x, self.y - other.y)
   
point1 = Point(10, 8)
point2 = Point(3, 2)

result = point1 - point2

print(result.x)  
print(result.y)  

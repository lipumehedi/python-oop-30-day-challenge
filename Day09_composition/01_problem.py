class Car:
    def __init__(self):
        self.engine = Engine()
        
    
class Engine:
    def start(self):
        return "Engine started"

car1 = Car()
print(car1.engine.start())
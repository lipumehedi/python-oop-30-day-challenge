class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "Animal makes a sound"
    
    
class Dog(Animal):
    pass

dog = Dog("Buddy")

print(dog.name)
print(dog.speak())
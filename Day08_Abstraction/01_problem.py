from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
    

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"
    
dog1 = Dog()
cat1 = Cat()

print(dog1.speak())
print(cat1.speak())
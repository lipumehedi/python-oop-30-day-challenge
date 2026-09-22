class Dog:
    def speak(self):
        return "Dog barks"
    

class Cat:
    def speak(self):
        return "Cat meows"
    
class Cow:
    def speak(self):
        return "Cow moos"
    
dog1 = Dog()
cat1 = Cat()
cow1 = Cow()   

print(dog1.speak())
print(cat1.speak())
print(cow1.speak())
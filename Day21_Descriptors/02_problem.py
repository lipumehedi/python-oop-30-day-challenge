class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__["age"]
    
    def __set__(self, instance, value):
        if value < 0:
           raise ValueError("Age cannot be negative")
        instance.__dict__["age"] = value
        
class Person:
    age = AgeDescriptor()
    
person = Person()
person.age = 30
print(f"Age: {person.age}")

# Test negative age
person.age = -5
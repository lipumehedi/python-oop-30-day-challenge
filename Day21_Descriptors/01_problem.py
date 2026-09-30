class NameDescriotor:
    def __get__(self, instance, owner):
        return instance.__dict__["name"]
    
    def __set__(self, instance, value):
        instance.__dict__["name"] = value
        
class Person:
    name = NameDescriotor()
    

person = Person()

person.name = "Lipu"

print(person.name)
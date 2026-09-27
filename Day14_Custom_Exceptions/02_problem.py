class InvalidAgeError(Exception):
    pass

class Person:
    def __init__(self, age):
        self.age = age
        
    def validate_age(self):
        if self.age < 18:
            raise InvalidAgeError("Age must be 18 or older.")
        

person = Person(16)

try:
    person.validate_age()
    print("Age is valid")

except InvalidAgeError as e:
    print("Error: ", e)
    

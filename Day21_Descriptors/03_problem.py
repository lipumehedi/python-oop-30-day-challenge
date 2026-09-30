class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__["email"]
    
    def __set__(self, instance, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        instance.__dict__["email"] = value
        
class Person:
    email = EmailDescriptor()

person = Person()
person.email = "lipu@gmail.com"

print(F"Email: {person.email}")

# Test invalid email
person.email = "lipu-example.com"
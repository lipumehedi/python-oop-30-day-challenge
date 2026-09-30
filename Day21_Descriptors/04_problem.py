class PasswordDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__["password"]
    
    def __set__(self, instance, value):
        if len(value) < 6:
            raise ValueError("Password must be at least 6 Characters")
        instance.__dict__["password"] = value
        
    def __delete__(self, instance):
        del instance.__dict__["password"]
        
        
class User:

    password = PasswordDescriptor()

user = User()
user.password = "python123"
print(f"Password: {user.password}")

del user.password
print("Password deleted successfully!")
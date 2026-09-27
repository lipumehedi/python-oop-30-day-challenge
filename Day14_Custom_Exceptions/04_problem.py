class InvalidLoginError(Exception):
    pass

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def validate_login(self):
        if self.username != "admin" or self.password != "1234":
            raise InvalidLoginError("Invalid username or password.")
        
login = Login("admin", "1234")

try:
    login.validate_login()
    print("Login successful")

except InvalidLoginError as e:
    print("Error: ", e)
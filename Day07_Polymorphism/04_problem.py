class EmailNotification:
    def __init__(self, message):
        self.message = message
        
    def send(self):
        return f"Email sent: {self.message}"
    
class SMSNotification:
    def __init__(self, message):
        self.message = message
    
    def send(self):
        return f"SMS sent: {self.message}"
    
class PushNotification:
    def __init__(self, message):
        self.message = message
        
    def send(self):
        return f"Push notification sent: {self.message}"
    
email = EmailNotification("Hello Mehedi")
sms = SMSNotification("Hello Mehedi")
push = PushNotification("Hello Mehedi")

print(email.send())
print(sms.send())
print(push.send())


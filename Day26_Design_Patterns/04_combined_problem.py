class EmailNotification:

    def send(self, message):
        return f"Email: {message}"


class SMSNotification:

    def send(self, message):
        return f"SMS: {message}"


class PushNotification:

    def send(self, message):
        return f"Push Notification: {message}"


class NotificationFactory:

    @staticmethod
    def create_notification(notification_type):

        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()


class NotificationManager:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.notification_strategy = None

    def set_strategy(self, strategy):
        self.notification_strategy = strategy

    def send_notification(self, message):
        if self.notification_strategy is None:
            raise ValueError("Notification strategy not set")
        return self.notification_strategy.send(message)


# Factory দিয়ে notification তৈরি
email = NotificationFactory.create_notification("email")
sms = NotificationFactory.create_notification("sms")
push = NotificationFactory.create_notification("push")


# Singleton Manager
manager1 = NotificationManager()
manager2 = NotificationManager()

print(manager1 is manager2)


# Strategy পরিবর্তন
manager1.set_strategy(email)
print(manager1.send_notification("Welcome Mehedi!"))

manager1.set_strategy(sms)
print(manager1.send_notification("Your OTP is 1234"))

manager1.set_strategy(push)
print(manager1.send_notification("You have a new message"))
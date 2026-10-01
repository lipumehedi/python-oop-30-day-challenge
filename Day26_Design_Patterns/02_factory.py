class EmailNotification:

    def send(self):
        return "Email notification sent"


class SMSNotification:

    def send(self):
        return "SMS notification sent"


class NotificationFactory:

    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
           return EmailNotification()
        elif notification_type == "sms":
           return SMSNotification()


notification1 = NotificationFactory.create_notification("email")
notification2 = NotificationFactory.create_notification("sms")

print(notification1.send())
print(notification2.send())
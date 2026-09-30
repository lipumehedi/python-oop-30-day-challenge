from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ¥{amount} using Credit Card"

class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid ¥{amount} using Credit Card"

credit_card = CreditCardPayment()
paypal = PayPalPayment()

print(credit_card.pay(5000))
print(paypal.pay(3000))
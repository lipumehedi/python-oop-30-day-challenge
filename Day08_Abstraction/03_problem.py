from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self, amount):
        self.amount =amount
        
    def pay(self):
        return f"Paid {self.amount} yen using Credit Card"
    

class PayPalPayment(Payment):
    def __init__(self, amount):
        self.amount = amount
        
    def pay(self):
        return f"Paid {self.amount} yen using PayPal"
    
class BankTransferPayment(Payment):
    def __init__(self, amount):
        self.amount = amount
        
    def pay(self):
        return f"Paid {self.amount} yen using Bank Transfer"
    
payment1 = CreditCardPayment(5000)
payment2 = PayPalPayment(5000)
payment3 = BankTransferPayment(5000)

print(payment1.pay())
print(payment2.pay())
print(payment3.pay())

payments = [payment1, payment2, payment3]

for payment in payments:
    print(payment.pay())
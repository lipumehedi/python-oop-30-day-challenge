class CreditCard:
    def __init__(self, amount):
        self.amount = amount
    
    def pay(self):
        return f"Paid {self.amount} yen using Credit Card"

class PayPal:
    def __init__(self, amount):
        self.amount = amount
        
    def pay(self):
        return f"Paid {self.amount} yen using PayPal"
    

class BankTransfer:
    def __init__(self, amount):
        self.amount = amount
        
    def pay(self):
        return f"Paid {self.amount} yen using Bank Transfer"
    

payment1 = CreditCard(5000)
payment2 = PayPal(5000)
payment3 = BankTransfer(5000)

print(payment1.pay())
print(payment2.pay())
print(payment3.pay())
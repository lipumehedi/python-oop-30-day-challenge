class CreditCardPayment:

    def pay(self, amount):
        self.amount = amount
        return f"Paid ¥{amount} using Credit Card"

class PayPalPayment:

    def pay(self, amount):
        self.amount = amount
        return f"Paid ¥{amount} using PayPal"


class BankTransferPayment:

    def pay(self, amount):
        self.amount = amount
        return f"Paid ¥{amount} using Bank Transfer"


class PaymentContext:

    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        self.payment_strategy.pay(amount)
        return self.payment_strategy.pay(amount)


credit_card = CreditCardPayment()
paypal = PayPalPayment()
bank_transfer = BankTransferPayment()

payment1 = PaymentContext(credit_card)
payment2 = PaymentContext(paypal)
payment3 = PaymentContext(bank_transfer)

print(payment1.pay(5000))
print(payment2.pay(3000))
print(payment3.pay(10000))
# Bad Design
"""
class Payment:

    def pay(self, payment_type, amount):
        if payment_type == "card":
            print(f"Paid ¥{amount} using Credit Card")

        elif payment_type == "paypal":
            print(f"Paid ¥{amount} using PayPal")
"""

#OCP

class Payment:
    def pay(self, amount):
        raise NotImplementedError


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ¥{amount} using Credit Card")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ¥{amount} using PayPal")


class BankTransferPayment(Payment):
    def pay(self, amount):
        print(f"Paid ¥{amount} using Bank Transfer")


def process_payment(payment, amount):
    payment.pay(amount)


credit_card = CreditCardPayment()
paypal = PayPalPayment()
bank_transfer = BankTransferPayment()

process_payment(credit_card, 5000)
process_payment(paypal, 3000)
process_payment(bank_transfer, 10000)
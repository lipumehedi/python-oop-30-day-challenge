class Money:
    def __init__(self, amount):
        self.amount = amount
        
    def __add__(self, other):
        return self.amount + other.amount
    
money1 = Money(500)
money2 = Money(300)

print(money1 + money2)
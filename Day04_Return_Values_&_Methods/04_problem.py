class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance 
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance!"
    

account1 = BankAccount("Mehedi", 10000)

print(account1.deposit(5000))
print(account1.withdraw(3000))
print(account1.withdraw(20000))
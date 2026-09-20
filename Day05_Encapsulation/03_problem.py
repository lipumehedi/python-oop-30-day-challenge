class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance 
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance 
        else:
            return "Insufficient balance!"

account1 = BankAccount("Mehedi", 10000)

print(account1.get_balance())

account1.deposit(5000)
print(account1.get_balance())

print(account1.withdraw(3000))
print(account1.get_balance())

print(account1.withdraw(20000))
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def show_balance(self):
        print(f"Holder: {self.account_holder} \nBalance: {self.balance}\n")
        
    def deposit(self, amount):
        self.balance += amount
            
    def withdraw(self, amount):
        self.balance -= amount
        
      
account1  = BankAccount("Mehedi", 10000)
account1.show_balance()

account1.deposit(5000)
account1.show_balance()

account1.withdraw(2000)
account1.show_balance()
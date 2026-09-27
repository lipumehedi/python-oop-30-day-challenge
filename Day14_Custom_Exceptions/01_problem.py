class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
        
    def withdraw(self, amount):
        if amount > self.balance:
         raise ValueError("Insufficient balance!")
        self.balance -= amount
        return self.balance
      
 

account = BankAccount(1000)

try:
    account.withdraw(300)
except ValueError as e:
    print("Error:", e)

print("Withdrawal successful. Remaining balance:", account.withdraw(300))
   

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance


account_1 = BankAccount("Anis Sarker", 250000.00)
account_2 = BankAccount("Mehedi Hasan", 240000.00)

print(f"Account 1: {account_1.account_holder}, Balance: {account_1.balance}")
print(f"Account 2: {account_2.account_holder}, Balance: {account_2.balance}")
    
    
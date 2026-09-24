class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number =account_number
        self.balance = balance
        
    def show_balance(self):
        return self.balance
    


class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account
        
    def show_account_info(self):
        return f"{self.name} -Account:{self.account.account_number} - Balance: {self.account.show_balance()} yen"
    

account1 = BankAccount("12345", 50000)

customer1 = Customer("Mehedi", account1)

print(customer1.show_account_info())
class Bank:
    bank_name = "ABC Bank"
    
    def __init__(self, account_holder):
        self.account_holder = account_holder
        
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        
account1 = Bank("Mehedi")
account2 = Bank("Rahim")

print(account1.bank_name)
print(account2.bank_name)

Bank.change_bank_name("XYZ Bank")

print(account1.bank_name)
print(account2.bank_name)
        
import unittest

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return self.balance
    
class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount(1000)
        result = account.deposit(500)
        self.assertEqual(result, 1500)
        
    def test_withdraw(self):
        account = BankAccount(1000)
        result = account.withdraw(300)
        self.assertEqual(result, 700)
        
    def test_get_balance(self):
        account = BankAccount(2000)
        result = account.get_balance()
        self.assertEqual(result, 2000)
        
if __name__ == "__main__":
    unittest.main()
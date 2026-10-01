import unittest


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        return self.balance


class TestBankAccount(unittest.TestCase):

    def test_valid_withdraw(self):
        account = BankAccount(1000)
        result = account.withdraw(300)
        self.assertEqual(result, 700)

    def test_insufficient_balance(self):
        account = BankAccount(1000)
        with self.assertRaises(ValueError):
            account.withdraw(1500)


if __name__ == "__main__":
    unittest.main()
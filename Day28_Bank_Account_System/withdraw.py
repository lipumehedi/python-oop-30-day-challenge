class BankAccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def show_account(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ¥{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("Deposit amount must be positive.")
            return self.balance

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("Insufficient balance.")
                return self.balance
        else:
            print("Withdrawal amount must be positive.")
            return self.balance

account = BankAccount("Mehedi", 10001, 50000)

account.deposit(10000)

new_balance = account.withdraw(15000)

print(f"After Withdrawal: ¥{new_balance}")
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        
Account_1 = BankAccount("Mehedi", "JP001", 250000)
Account_2 = BankAccount("Rahim", "JP002", 180000)

print(
    f"Holder: {Account_1.account_holder}\n"
    f"Number: {Account_1.account_number}\n"
    f"Balance: {Account_1.balance}\n"
)

print(
    f"Holder: {Account_2.account_holder}\n"
    f"Number: {Account_2.account_number}\n"
    f"Balance: {Account_2.balance}\n"
)

Account_1.balance = 300000

print(
    f"Holder: {Account_1.account_holder}\n"
    f"Number: {Account_1.account_number}\n"
    f"Balance: {Account_1.balance}\n"
)

print(
    f"Holder: {Account_2.account_holder}\n"
    f"Number: {Account_2.account_number}\n"
    f"Balance: {Account_2.balance}"
)
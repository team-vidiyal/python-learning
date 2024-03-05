class BankAccount:
    def __init__(self, account_number, account_holder_name, address, amount):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.address = address
        self.amount = amount

    def __str__(self):
        return f"[BankAccount = {self.account_number}, {self.account_holder_name}, {self.address}, {self.amount}]"


francis_account = BankAccount(123456, 'Francis', 'MD', 100000)

print(francis_account)

# account number, account name, "address, amount
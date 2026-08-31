class Account:
    def __init__(self, account_id, account_type, balance):
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def change_account_type(self, new_account_type):
        self.account_type = new_account_type
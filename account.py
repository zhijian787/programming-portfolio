class Account:
    def __init__(self, account_id, account_type, balance):
         self.__account_id = account_id
         self.__account_type = account_type
         self.__balance = balance

    @property
    def account_id(self):
        return self.__account_id

    @property
    def account_type(self):
        return self.__account_type

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
         self.__balance += amount

    def withdraw(self, amount):
     if amount <= 0:
        return

     if amount <= self.__balance:
        self.__balance -= amount
     else:
        print("Insufficient funds")

    def change_account_type(self, new_account_type):
        self.__account_type = new_account_type

    def __str__(self):
        return f"Account {self.account_id}: {self.account_type}, Balance: ${self.balance}"

    def __repr__(self):
        return f"Account('{self.account_id}', '{self.account_type}', {self.balance})"
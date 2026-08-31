from client import Client
from account import Account
from transaction import Transaction
from branch import Branch
client1 = Client("C001", "zhijianhuang", "a1979239@adelaide.edu.au")
print(client1.name)
print(client1.contact)
client1.update_contact("2531553681@qq.com")
print(client1.contact)

account1 = Account("A001", "Saving", 1000)
print(account1.balance)
account1.deposit(500)
print(account1.balance)
account1.withdraw(200)
print(account1.balance)
account1.withdraw(2000)  #if not enough
client2 = Client("C002", "xiaoyu li", "xiaoyu.li@example.com")
client3 = Client("C003", "aki", "aki@example.com")
print(client2.name)
print(client3.name)
print(client2.contact)
client2.update_contact("zhijianhuang@gmail.com")
print(client2.contact)
account2 = Account("A002", "Checking", 2000)
account3 = Account("A003", "Saving", 3000)

print(account2.balance)
print(account3.balance)
account2.deposit(1000)
print(account2.balance)
account3.withdraw(500)
print(account3.balance)
print(account1.balance)
print(account2.balance)
account1.deposit(300)
print(account1.balance)
print(account2.balance)
print(account2.account_type)
account2.change_account_type("Business")
print(account2.account_type)
transaction1 = Transaction("T001", "Deposit", 500, "Test transaction")
print(transaction1.status)
print(transaction1.status)
transaction1.update_status()
print(transaction1.status)
transaction1.cancel_transaction()
print(transaction1.status)
transaction2 = Transaction("T002", "Withdrawal", 200, "Test transaction 2")
print(transaction2.status)

transaction2.cancel_transaction()

print(transaction2.status)
print(transaction2.description)

transaction2.update_description("Updated transaction description")

print(transaction2.description)

branch1 = Branch("B001", "Adelaide Branch", "Adelaide CBD", "0800000000")

print(branch1.is_open)

branch1.open_branch()
print(branch1.is_open)

branch1.close_branch()
print(branch1.is_open)

print(branch1.phone_number)
branch1.update_phone_number("0811111111")
print(branch1.phone_number)

print(client1)
print(account1)
print(transaction1)
print(branch1)

print(repr(client1))
print(repr(account1))
print(repr(transaction1))
print(repr(branch1))
account1.deposit(-500)
print(account1.balance)

account1.withdraw(-300)
print(account1.balance)
client1.add_account(account1)
client1.add_account(account2)

print(len(client1.accounts))

for account in client1.accounts:
    print(account)

client1.remove_account(account2)

print(len(client1.accounts))

branch1.add_client(client1)
branch1.add_client(client2)

print(len(branch1.clients))

for client in branch1.clients:
    print(client)

branch1.remove_client(client2)

print(len(branch1.clients))
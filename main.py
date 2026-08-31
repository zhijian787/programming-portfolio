from client import Client
from account import Account
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
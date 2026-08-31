from client import Client
client1 = Client("A001", "zhijianhuang", "a1979239@adelaide.edu.au")
print(client1.name)
print(client1.contact)
client1.update_contact("2531553681@qq.com")
print(client1.contact)
class Client:
    def __init__(self,client_id,name,contact):
        self.client_id = client_id
        self.name = name
        self.contact = contact
    def update_contact(self, new_contact):
        self.contact = new_contact

    def __str__(self):
        return f"Client {self.client_id}: {self.name}, Contact: {self.contact}"

    def __repr__(self):
        return f"Client('{self.client_id}', '{self.name}', '{self.contact}')"
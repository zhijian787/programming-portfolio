class Client:
    def __init__(self,client_id,name,contact):
        self.client_id = client_id
        self.name = name
        self.contact = contact
    def update_contact(self, new_contact):
        self.contact = new_contact
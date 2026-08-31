class Client:
    def __init__(self, client_id, name, contact):
        self.__client_id = client_id
        self.__name = name
        self.__contact = contact
        self.__accounts = []

    @property
    def client_id(self):
        return self.__client_id

    @property
    def name(self):
        return self.__name

    @property
    def contact(self):
        return self.__contact

    @property
    def accounts(self):
        return self.__accounts

    def update_contact(self, new_contact):
        if new_contact:
            self.__contact = new_contact

    def add_account(self, account):
        if account not in self.__accounts:
            self.__accounts.append(account)

    def remove_account(self, account):
        if account in self.__accounts:
            self.__accounts.remove(account)
    def __str__(self):
        return f"Client {self.client_id}: {self.name}, Contact: {self.contact}"

    def __repr__(self):
        return f"Client('{self.client_id}', '{self.name}', '{self.contact}')"
class Branch:
    def __init__(self, branch_number, branch_name, location, phone_number, is_open=False):
        self.__branch_number = branch_number
        self.__branch_name = branch_name
        self.__location = location
        self.__phone_number = phone_number
        self.__is_open = is_open
        self.__clients = []

    @property
    def branch_number(self):
        return self.__branch_number

    @property
    def branch_name(self):
        return self.__branch_name

    @property
    def location(self):
        return self.__location

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def is_open(self):
        return self.__is_open

    @property
    def clients(self):
        return self.__clients

    def open_branch(self):
        self.__is_open = True

    def close_branch(self):
        self.__is_open = False

    def update_phone_number(self, new_phone_number):
        if new_phone_number:
            self.__phone_number = new_phone_number

    def add_client(self, client):
        if client not in self.__clients:
            self.__clients.append(client)

    def remove_client(self, client):
        if client in self.__clients:
            self.__clients.remove(client)

    def __str__(self):
        return (
            f"Branch {self.branch_number}: "
            f"{self.branch_name}, {self.location}, Open: {self.is_open}"
        )

    def __repr__(self):
        return (
            f"Branch('{self.branch_number}', "
            f"'{self.branch_name}', "
            f"'{self.location}', "
            f"'{self.phone_number}', "
            f"{self.is_open})"
        )
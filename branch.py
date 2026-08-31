class Branch:
    def __init__(self, branch_number, branch_name, location, phone_number, is_open=False):
        self.branch_number = branch_number
        self.branch_name = branch_name
        self.location = location
        self.phone_number = phone_number
        self.is_open = is_open

    def open_branch(self):
        self.is_open = True

    def close_branch(self):
        self.is_open = False

    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
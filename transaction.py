class Transaction:
    def __init__(self, transaction_identifier, transaction_type, amount, description, status="Pending"):
        self.transaction_identifier = transaction_identifier
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.status = status

    def update_status(self):
        if self.status == "Pending":
            self.status = "Processed"

    def cancel_transaction(self):
        if self.status == "Pending":
            self.status = "Cancelled"

    def update_description(self, new_description):
        self.description = new_description

    def __str__(self):
        return f"Transaction {self.transaction_identifier}: {self.transaction_type}, Amount: ${self.amount}, Status: {self.status}"

    def __repr__(self):
        return f"Transaction('{self.transaction_identifier}', '{self.transaction_type}', {self.amount}, '{self.description}', '{self.status}')"
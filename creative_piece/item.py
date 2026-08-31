class Item:
    def __init__(self, name, category, quantity):
        self.__name = name
        self.__category = category
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def quantity(self):
        return self.__quantity

    def add_quantity(self, amount):
        if amount > 0:
            self.__quantity += amount

    def remove_quantity(self, amount):
        if amount > 0 and amount <= self.__quantity:
            self.__quantity -= amount
            return True
        return False

    def __str__(self):
        return f"{self.name} ({self.category}) - Quantity: {self.quantity}"

    def __repr__(self):
        return f"Item('{self.name}', '{self.category}', {self.quantity})"
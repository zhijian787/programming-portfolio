class Rune:
    def __init__(self, rune_type, amount):
        self.__rune_type = rune_type
        self.__amount = amount

    @property
    def rune_type(self):
        return self.__rune_type

    @property
    def amount(self):
        return self.__amount

    def add(self, amount):
        if amount > 0:
            self.__amount += amount

    def consume(self, amount):
        if amount > 0 and amount <= self.__amount:
            self.__amount -= amount
            return True
        return False

    def __str__(self):
        return f"{self.rune_type}: {self.amount}"
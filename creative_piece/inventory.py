class Inventory:
    def __init__(self, owner):
        self.__owner = owner
        self.__items = []

    @property
    def owner(self):
        return self.__owner

    @property
    def items(self):
        return self.__items

    def add_item(self, item):
        if item not in self.__items:
            self.__items.append(item)

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            return True
        return False

    def find_item(self, name):
        for item in self.__items:
            if item.name == name:
                return item
        return None

    def __str__(self):
        return f"{self.owner}'s Inventory - {len(self.items)} items"
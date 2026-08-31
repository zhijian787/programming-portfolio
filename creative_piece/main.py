from item import Item
from inventory import Inventory


sword = Item("Iron Sword", "Weapon", 1)
potion = Item("Health Potion", "Consumable", 5)
shield = Item("Wooden Shield", "Armour", 1)

inventory = Inventory("Player")

inventory.add_item(sword)
inventory.add_item(potion)
inventory.add_item(shield)

print(inventory)

for item in inventory.items:
    print(item)

potion.add_quantity(3)
print(potion)

potion.remove_quantity(2)
print(potion)

found_item = inventory.find_item("Iron Sword")
print(found_item)

inventory.remove_item(shield)

print(inventory)

for item in inventory.items:
    print(item)
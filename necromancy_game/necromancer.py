from undead import Undead


class Necromancer:
    def __init__(self, name):
        self.__name = name
        self.__runes = []
        self.__undead_army = []

    @property
    def name(self):
        return self.__name

    @property
    def runes(self):
        return self.__runes

    @property
    def undead_army(self):
        return self.__undead_army

    def add_rune(self, rune):
        self.__runes.append(rune)

    def add_undead(self, undead):
        self.__undead_army.append(undead)

    def summon_undead(self, rune, cost, name, undead_type, health, attack_power):
        if rune.consume(cost):
            undead = Undead(name, undead_type, health, attack_power)
            self.__undead_army.append(undead)
            return undead

        return None

    def __str__(self):
        return (
            f"Necromancer {self.name} - "
            f"Runes: {len(self.runes)}, "
            f"Undead: {len(self.undead_army)}"
        )
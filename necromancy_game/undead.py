class Undead:
    def __init__(self, undead_id, name, undead_type, health, attack_power):
        self.__undead_id = undead_id
        self.__name = name
        self.__undead_type = undead_type
        self.__health = health
        self.__attack_power = attack_power
        self.__is_alive = True

    @property
    def undead_id(self):
        return self.__undead_id

    @property
    def name(self):
        return self.__name

    @property
    def undead_type(self):
        return self.__undead_type

    @property
    def health(self):
        return self.__health

    @property
    def attack_power(self):
        return self.__attack_power

    @property
    def is_alive(self):
        return self.__is_alive

    def take_damage(self, amount):
        if amount > 0:
            self.__health -= amount

            if self.__health <= 0:
                self.__health = 0
                self.__is_alive = False

    def heal(self, amount):
        if amount > 0 and self.__is_alive:
            self.__health += amount

    def attack(self):
        if self.__is_alive:
            return self.__attack_power
        return 0

    def __str__(self):
        return (
            f"{self.name} ({self.undead_type}) - "
            f"Health: {self.health}, Attack: {self.attack_power}"
        )
class Item:
    def __init__(self, name):
        self.name = name

    def apply(self, player):
        pass

class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion")

    def apply(self, player):
        player.health += 1

class Sword(Item):
    def __init__(self):
        super().__init__("Sword")

    def apply(self, player):
        player.damage += 1

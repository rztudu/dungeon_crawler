class Item:
    def __init__(
        self,
        name,
        description,
        rarity="Common"
    ):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.amount = 1

    def apply(self, player):
        pass
'''
class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion", "heals player")

    def apply(self, player):
        player.health += 1

class Sword(Item):
    def __init__(self):
        super().__init__("Sword", "increases damge")

    def apply(self, player):
        player.damage += 1
'''

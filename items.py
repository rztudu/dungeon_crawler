from item import Item

class DamageUpgrade(Item):

    def __init__(self):
        super().__init__(
            "Iron Sword",
            "+1 Damage"
        )

    def apply(self, player):
        player.damage += 1

class HealthUpgrade(Item):

    def __init__(self):
        super().__init__(
            "Ruby",
            "+5 Max HP"
        )

    def apply(self, player):
        player.max_health += 5
        player.health += 5

class SpeedUpgrade(Item):

    def __init__(self):
        super().__init__(
            "Boots",
            "+20 Speed"
        )

    def apply(self, player):
        player.speed += 20

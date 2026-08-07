import random

from items import (
    DamageUpgrade,
    HealthUpgrade,
    SpeedUpgrade,
)


def generate_loot():

    loot_table = [
        (DamageUpgrade, 50),
        (HealthUpgrade, 30),
        (SpeedUpgrade, 20),
    ]

    roll = random.randint(1, 100)

    current = 0

    for item, chance in loot_table:
        current += chance

        if roll <= current:
            return item()

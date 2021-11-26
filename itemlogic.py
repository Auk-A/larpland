from dataclasses import dataclass


# Items and weapons
@dataclass
class Item:
    def __init__(self, name):
        self.name = name
        self.coin_value = None


@dataclass
class Weapon(Item):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed
        self.damage = 10


@dataclass
class RangedWeapon(Weapon):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.range = 50


@dataclass
class MeleeWeapon(Weapon):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.range = 10


@dataclass
class MagicWeapon(Weapon):
    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.range = 20

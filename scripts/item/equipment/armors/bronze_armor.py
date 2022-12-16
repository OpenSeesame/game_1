from scripts.item.equipment.armor import Armor
from constants.names import Names

class BronzeArmor(Armor):
    Name = Names.BRONZE_ARMOR
    Hp = 100
    def __init__(self, name=Name, hp=Hp):
        super().__init__(name, hp)

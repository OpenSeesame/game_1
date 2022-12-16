from scripts.item.equipment.armor import Armor
from constants.names import Names

class Hadaka(Armor):
    Name = Names.HADAKA
    Hp = 0
    def __init__(self, name=Name, hp=Hp):
        super().__init__(name, hp)

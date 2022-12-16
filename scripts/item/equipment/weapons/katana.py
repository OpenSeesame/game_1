from scripts.item.equipment.weapon import Weapon
from constants.names import Names

class Katana(Weapon):
    Name = Names.KATANA
    Atk = 10
    def __init__(self, name=Name, atk=Atk):
        super().__init__(name, atk)
from scripts.item.equipment.weapon import Weapon
from constants.names import Names

class Sude(Weapon):
    Name = Names.SUDE_W
    Atk = 0
    def __init__(self, name=Name, atk=Atk):
        super().__init__(name, atk)
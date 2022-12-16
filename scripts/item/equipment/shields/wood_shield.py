from scripts.item.equipment.shield import Shield
from constants.names import Names

class WoodShield(Shield):
    Name = Names.WOOD_SHIELD
    Ar = 5
    def __init__(self, name=Name, ar=Ar):
        super().__init__(name, ar)
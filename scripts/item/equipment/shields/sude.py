from scripts.item.equipment.shield import Shield
from constants.names import Names

class Sude(Shield):
    Name = Names.SUDE_S
    Ar = 0
    def __init__(self, name=Name, ar=Ar):
        super().__init__(name, ar)
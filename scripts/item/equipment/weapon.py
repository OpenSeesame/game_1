from scripts.item.equipment.equipment import Equipment
from constants.names import Names

class Weapon(Equipment):
    Name = Names.SUDE_W
    Atk = 0
    def __init__(self, name=Name, atk=Atk):
        super().__init__(name)
        self.__atk = atk

    def get_atk(self):
        return self.__atk
    def set_atk(self, atk):
        self.__atk = atk   
from scripts.item.equipment.equipment import Equipment
from constants.names import Names

class Armor(Equipment):
    Name = Names.HADAKA
    Hp = 0
    def __init__(self, name=Name, hp=Hp):
        super().__init__(name)
        self.__hp = hp

    def get_hp(self):
        return self.__hp
    def set_hp(self, hp):
        self.__hp = hp   
from scripts.equipment.equipment import Equipment
class Armor(Equipment):
    def __init__(self, name='Hadaka', hp=0):
        super().__init__(name)
        self.__hp = hp

    def get_hp(self):
        return self.__hp
    def set_hp(self, hp):
        self.__hp = hp   
from scripts.equipment.equipment import Equipment
class Weapon(Equipment):
    def __init__(self, name='Sude', atk=0):
        super().__init__(name)

        self.__atk = atk

    def get_atk(self):
        return self.__atk
    def set_atk(self, atk):
        self.__atk = atk   
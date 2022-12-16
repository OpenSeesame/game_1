from scripts.item.equipment.equipment import Equipment
from constants.names import Names

class Shield(Equipment):
    Name = Names.SUDE_S
    Ar = 0
    def __init__(self, name=Name, ar=Ar):
        super().__init__(name)
        self.__ar = ar

    def get_ar(self):
        return self.__ar
    def set_ar(self, ar):
        self.__ar = ar   
from scripts.equipment.equipment import Equipment
class Shield(Equipment):
    def __init__(self, name='Sude', ar=0):
        super().__init__(name)
        self.__ar = ar

    def get_ar(self):
        return self.__ar
    def set_ar(self, ar):
        self.__ar = ar   
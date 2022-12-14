class Equipment:
    def __init__(self, name='weapon_name'):
        self.__name = name

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
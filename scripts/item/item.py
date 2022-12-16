class Item():
    Name = ''
    def __init__(self, name=Name):
        self.__name = name

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
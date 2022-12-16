class Character:
    Name = ''
    Hp = 500
    Mp = 50
    Atk = 50
    Ar = 0
    Mr = 0
    def __init__(self, name=Name, hp=Hp, mp=Mp, atk=Atk, ar=Ar, mr=Mr):
        self.__name = name
        self.__max_hp = hp
        self.__hp = hp
        self.__max_mp = mp
        self.__mp = mp
        self.__atk = atk
        self.__ar = ar
        self.__mr = mr

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_max_hp(self):
        return self.__max_hp
    def set_max_hp(self, max_hp):
        self.__max_hp = max_hp

    def get_hp(self):
        return self.__hp
    def set_hp(self, hp):
        self.__hp = hp

    def get_max_mp(self):
        return self.__max_mp
    def set_max_mp(self, max_mp):
        self.__max_mp = max_mp   

    def get_mp(self):
        return self.__mp
    def set_mp(self, mp):
        self.__mp = mp   

    def get_atk(self):
        return self.__atk
    def set_atk(self, atk):
        self.__atk = atk   

    def get_ar(self):
        return self.__ar
    def set_ar(self, ar):
        self.__ar = ar   

    def get_mr(self):
        return self.__mr
    def set_mr(self, mr):
        self.__mr = mr
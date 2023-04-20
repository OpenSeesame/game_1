from scripts.item.item import Item

class Spell(Item):
    Name=''
    ConsMp=0
    AdditionalDamage=0
    def __init__(self, name=Name, cons_mp=ConsMp, additional_damage=AdditionalDamage):
        super().__init__(name)
        self.__additional_damage = additional_damage
        self.__cons_mp = cons_mp

    def get_additional_damage(self):
        return self.__additional_damage

    def get_cons_mp(self):
        return self.__cons_mp

    def set_additional_damage(self, additional_damage):
        self.__additional_damage =  additional_damage

    def set_cons_mp(self, cons_mp):
        self.__cons_mp =  cons_mp
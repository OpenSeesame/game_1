from scripts.constants.constants import Constants
from scripts.dialog.dialog import Dialog
from scripts.dialog.battle_dialog import BattleDialog
from scripts.system.calculate import Calculate

from scripts.character.character import Character
from scripts.equipment.weapon import Weapon
from scripts.equipment.armor import Armor
from scripts.equipment.shield import Shield

class Player(Character):
    Hp = 500
    Mp = 50
    Atk = 50
    Ar = 0
    Mr = 0
    def __init__(self, name="", hp=Hp, mp=Mp, atk=Atk, ar=Ar, mr=Mr, weapon=Weapon(), shield=Shield(), armor=Armor()):
        super().__init__(name, hp, mp, atk, ar, mr)
        self.__weapon = weapon
        self.__armor = armor
        self.__shield = shield
        self.set_atk(self.get_atk() + weapon.get_atk())
        self.set_max_hp(self.get_max_hp() + armor.get_hp())
        self.set_hp(self.get_hp() + armor.get_hp())
        self.set_ar(self.get_ar() + shield.get_ar())

    def equip(self, equipment):
        if isinstance(equipment, Weapon):
            self.set_atk(self.get_atk() + equipment.get_atk())
            self.set_weapon(equipment)
        if isinstance(equipment, Armor):
            self.set_max_hp(self.get_max_hp() + equipment.get_hp())
            self.set_hp(self.get_hp() + equipment.get_hp())
            self.set_armor(equipment)
        if isinstance(equipment, Shield):
            self.set_ar(self.get_ar() + equipment.get_ar())
            self.set_shield(equipment)

        print(Dialog.equiqqed(self, equipment))
    
    def attack(self, enemy):
        # calculate damage
        damage = Calculate.calc_damage(self.get_atk(), enemy.get_ar())

        if damage > enemy.get_hp():
            enemy.set_hp(Constants.INT_ZERO)
        else:
            enemy.set_hp(enemy.get_hp() - damage)

        print(BattleDialog.attacked(self, enemy, damage))


    def get_weapon(self):
        return self.__weapon
    def set_weapon(self, weapon):
        self.__weapon = weapon
    def get_armor(self):
        return self.__armor
    def set_armor(self, armor):
        self.__armor = armor
    def get_shield(self):
        return self.__shield
    def set_shield(self, shield):
        self.__shield = shield
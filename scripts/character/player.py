from constants.constants import Constants
from scripts.dialog.dialog import Dialog
from scripts.dialog.battle_dialog import BattleDialog
from scripts.system.calculate import Calculate

from scripts.character.character import Character
from scripts.item.equipment.weapons.sude import Sude as SudeW
from scripts.item.equipment.shields.sude import Sude as SudeS
from scripts.item.equipment.armors.hadaka import Hadaka
from scripts.item.equipment.weapon import Weapon
from scripts.item.equipment.armor import Armor
from scripts.item.equipment.shield import Shield

class Player(Character):
    Name = ''
    Hp = 500
    Mp = 50
    Atk = 50
    Ar = 0
    Mr = 0
    Weapon = SudeW()
    Shield = SudeS()
    Armor = Hadaka()
    Guarding = False

    def __init__(self, name=Name, hp=Hp, mp=Mp, atk=Atk, ar=Ar, mr=Mr, weapon=Weapon, shield=Shield, armor=Armor, guarding=Guarding):
        super().__init__(name, hp, mp, atk, ar, mr)
        self.__equip_weapon(weapon)
        self.__equip_shield(shield)
        self.__equip_armor(armor)
        self.__guarding = guarding

    ### action (s) ###

    def equip(self, equipment, with_dialog=Constants.WITHOUT_DIALOG):
        if with_dialog == Constants.WITH_DIALOG:
            print(Dialog.equipped(self, equipment))

        if isinstance(equipment, Weapon):
            self.__unequip_weapon()
            self.__equip_weapon(equipment)
        if isinstance(equipment, Shield):
            self.__unequip_shield()
            self.__equip_shield(equipment)
        if isinstance(equipment, Armor):
            self.__unequip_armor()
            self.__equip_armor(equipment)

    def unequip(self, parts=Constants.ALL, with_dialog=Constants.WITHOUT_DIALOG):
        if parts == Constants.ALL:
            if with_dialog == Constants.WITH_DIALOG:
                print(Dialog.unequipped(self, self.get_weapon()))
                print(Dialog.unequipped(self, self.get_shield()))
                print(Dialog.unequipped(self, self.get_armor()))
            self.__unequip_weapon()
            self.__unequip_shield()
            self.__unequip_armor()

        elif parts == Constants.WEAPON:
            if with_dialog == Constants.WITH_DIALOG:
                print(Dialog.unequipped(self, self.get_weapon()))
            self.__unequip_weapon()

        elif parts == Constants.SHIELD:
            if with_dialog == Constants.WITH_DIALOG:
                print(Dialog.unequipped(self, self.get_shield()))
            self.__unequip_shield()

        elif parts == Constants.ARMOR:
            if with_dialog == Constants.WITH_DIALOG:
                print(Dialog.unequipped(self, self.get_armor()))
            self.__unequip_armor()

    def attack(self, enemy, with_dialog=Constants.WITHOUT_DIALOG):
        # calculate damage
        damage = Calculate.calc_damage_ar(self, enemy)

        if damage > enemy.get_hp():
            enemy.set_hp(Constants.INT_ZERO)
        else:
            enemy.set_hp(enemy.get_hp() - damage)

        if with_dialog == Constants.WITH_DIALOG:
            print(BattleDialog.attacked(self, enemy, damage))
 
    def guard(self, with_dialog=Constants.WITHOUT_DIALOG):
        self.set_guarding(True)

        if with_dialog == Constants.WITH_DIALOG:
            print(BattleDialog.guarding(self))
    
    def unguard(self, with_dialog=Constants.WITHOUT_DIALOG):
        self.set_guarding(False)

        if with_dialog == Constants.WITH_DIALOG:
            self
   
    # with dialog
    def equip_with_dialog(self, equipment):
        self.equip(equipment, Constants.WITH_DIALOG)

    def unequip_with_dialog(self, parts):
        self.unequip(parts, Constants.WITH_DIALOG)
   
    def attack_with_dialog(self, enemy):
        self.attack(enemy, Constants.WITH_DIALOG)
    
    def guard_with_dialog(self):
        self.guard(Constants.WITH_DIALOG)

    def unguard_with_dialog(self):
        self.unguard(Constants.WITH_DIALOG)

    ### action (e) ###

    # getter, setter
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

    def is_guarding(self):
        return self.__guarding
    def set_guarding(self, guarding):
        self.__guarding = guarding

    # private method
    def __equip_weapon(self, weapon):
            self.set_atk(self.get_atk() + weapon.get_atk())
            self.set_weapon(weapon)
    def __equip_shield(self, shield):
            self.set_ar(self.get_ar() + shield.get_ar())
            self.set_shield(shield)
    def __equip_armor(self, armor):
            self.set_max_hp(self.get_max_hp() + armor.get_hp())
            self.set_armor(armor)

    def __unequip_weapon(self):
            self.set_atk(self.get_atk() - self.get_weapon().get_atk())
            self.__equip_weapon(SudeW())
    def __unequip_shield(self):
            self.set_ar(self.get_ar() - self.get_shield().get_ar())
            self.__equip_shield(SudeS())
    def __unequip_armor(self):
            self.set_max_hp(self.get_max_hp() - self.get_armor().get_hp())
            if (self.get_hp() > self.get_max_hp()):
                self.set_hp(self.get_max_hp())
            self.__equip_armor(Hadaka())

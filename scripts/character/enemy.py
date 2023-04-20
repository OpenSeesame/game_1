from constants.constants import Constants
from scripts.dialog.battle_dialog import BattleDialog
from scripts.character.character import Character
from scripts.system.calculate import Calculate

class Enemy(Character):
    Name = ''
    Hp = 100
    Mp = 50
    Atk = 25
    Ar = 10
    Mr = 0
    Exp = 0
    Guarding = False

    def __init__(self, name=Name, hp=Hp, mp=Mp, atk=Atk, ar=Ar, mr=Mr, exp=Exp, guarding=Guarding):
        super().__init__(name, hp, mp, atk, ar, mr)
        self.__guarding = guarding
        self.__exp = exp

    def attack(self, player, with_dialog=Constants.WITHOUT_DIALOG):
        # calculate damage
        damage = Calculate.calc_damage_ar(self, player)

        if damage > player.get_hp():
            player.set_hp(Constants.INT_ZERO)
        else:
            player.set_hp(player.get_hp() - damage)

        if with_dialog == Constants.WITH_DIALOG:
            print(BattleDialog.attacked(self, player, damage))
    
    def attack_with_dialog(self, player):
        self.attack(player, Constants.WITH_DIALOG)

    def get_exp(self):
        return self.__exp
    def set_exp(self, exp):
        self.__exp = exp
    def is_guarding(self):
        return self.__guarding
    def set_guarding(self, guarding):
        self.__guarding = guarding
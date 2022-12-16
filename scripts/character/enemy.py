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
    def __init__(self, name=Name, hp=Hp, mp=Mp, atk=Atk, ar=Ar, mr=Mr):
        super().__init__(name, hp, mp, atk, ar, mr)

    def attack(self, player, with_dialog=Constants.WITHOUT_DIALOG):
        # calculate damage
        damage = Calculate.calc_damage(self.get_atk(), player.get_ar())

        if damage > player.get_hp():
            player.set_hp(Constants.INT_ZERO)
        else:
            player.set_hp(player.get_hp() - damage)

        if with_dialog == Constants.WITH_DIALOG:
            print(BattleDialog.attacked(self, player, damage))
    
    def attack_with_dialog(self, player):
        self.attack(player, Constants.WITH_DIALOG)
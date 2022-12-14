from scripts.constants.constants import Constants
from scripts.dialog.battle_dialog import BattleDialog
from scripts.character.character import Character
from scripts.system.calculate import Calculate

class Enemy(Character):
    Hp = 100
    Mp = 50
    Atk = 25
    Ar = 10
    Mr = 0
    def __init__(self, name="TEKI", hp=Hp, mp=Mp, atk=Atk, ar=Ar, mr=Mr):
        super().__init__(name, hp, mp, atk, ar, mr)

    def attack(self, player):
        # calculate damage
        damage = Calculate.calc_damage(self.get_atk(), player.get_ar())

        if damage > player.get_hp():
            player.set_hp(Constants.INT_ZERO)
        else:
            player.set_hp(player.get_hp() - damage)

        print(BattleDialog.attacked(self, player, damage))
from constants.constants import Constants
from scripts.system.start import Start
from scripts.character.enemy import Enemy
import scripts.character.enemies as enemies
import scripts.item.equipment.weapons as weapons
import scripts.item.equipment.shields as shields
import scripts.item.equipment.armors as armors
from scripts.character.player import Player
from scripts.dialog.battle_dialog import BattleDialog


class Main:
    def __init__(self):
        self.test()

    def test(self):
        player = Player('Taro')
        Start(player)

        player.equip(weapons.Katana(), Constants.WITH_DIALOG)
        player.equip(shields.WoodShield(), Constants.WITH_DIALOG)
        player.equip(armors.BronzeArmor(), Constants.WITH_DIALOG)

        print(BattleDialog.status(player))

        player.unequip(Constants.WEAPON, Constants.WITH_DIALOG)

        print(BattleDialog.status(player))
        print(BattleDialog.equipment(player))

        slime = enemies.Slime()

        player.attack_with_dialog(slime)
        slime.attack_with_dialog(player)


Main()
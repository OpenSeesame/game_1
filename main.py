from constants.constants import Constants
from scripts.system.start import Start
from scripts.system.battle import Battle
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

        Battle(player, enemies.Slime())

Main()
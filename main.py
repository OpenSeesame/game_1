from scripts.constants.constants import Constants
from scripts.system.start import Start
from scripts.character.enemy import Enemy
import scripts.character.enemies as enemies
from scripts.character.player import Player
from scripts.equipment.weapon import Weapon
from scripts.equipment.armor import Armor
from scripts.equipment.shield import Shield
from scripts.dialog.battle_dialog import BattleDialog


class Main:
    def __init__(self):
        self.test()

    def test(self):
        player = Player('Taro')
        Start(player)

        katana = Weapon('Katana', 10)
        bronze_armor = Armor('Bronze Armor', 100)
        wood_shield = Shield('Wood Shield', 5)

        player.equip(katana)
        player.equip(bronze_armor)
        player.equip(wood_shield)

        slime = enemies.Slime()

        player.attack(slime)
        slime.attack(player)


Main()
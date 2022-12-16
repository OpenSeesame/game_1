from constants.constants import Constants
from scripts.dialog.dialog import Dialog

class BattleDialog(Dialog):
    def __init__(self):
        super().__init__()
    
    def attacked(player, enemy, damage):
        s = str(player.get_name()) + "'s attack!!" + Constants.BR
        s += str(enemy.get_name()) + ' takes ' + str(damage) + ' damage!!'

        s = BattleDialog.word_in_asterisk(s)
        return s
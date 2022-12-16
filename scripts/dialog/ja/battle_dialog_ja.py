from constants.constants import Constants
from scripts.dialog.ja.dialog_ja import Dialog

class BattleDialog(Dialog):
    def __init__(self):
        super().__init__()
    
    def attacked(player, enemy, damage):
        s = str(player.get_name()) + "のこうげき!!" + Constants.BR
        s += str(enemy.get_name()) + 'は' + str(damage) + 'ダメージをうけた!!'

        s = BattleDialog.word_in_asterisk(s)
        return s
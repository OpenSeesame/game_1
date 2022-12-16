from constants.constants import Constants
from scripts.dialog.dialog import Dialog 
from scripts.dialog.en.battle_dialog_en import BattleDialog as BattleDialogEn
from scripts.dialog.ja.battle_dialog_ja import BattleDialog as BattleDialogJa

class BattleDialog(Dialog):
    def __init__(self):
        super().__init__()
    
    def attacked(player, enemy, damage):
        if Constants.LANG == Constants.LANG_EN:
            s = BattleDialogEn.attacked(player, enemy, damage)
        elif Constants.LANG == Constants.LANG_JA:
            s = BattleDialogJa.attacked(player, enemy, damage)
        return s
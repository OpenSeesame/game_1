from constants.constants import Constants
from scripts.dialog.dialog import Dialog 
from scripts.dialog.en.battle_dialog_en import BattleDialog as BattleDialogEn
from scripts.dialog.ja.battle_dialog_ja import BattleDialog as BattleDialogJa

class BattleDialog(Dialog):
    def __init__(self):
        super().__init__()
    
    def command():
        if Constants.LANG == Constants.LANG_EN:
            s = BattleDialogEn.command()
        elif Constants.LANG == Constants.LANG_JA:
            s = BattleDialogJa.command()
        return s

    def select_command():
        if Constants.LANG == Constants.LANG_EN:
            s = BattleDialogEn.select_command()
        elif Constants.LANG == Constants.LANG_JA:
            s = BattleDialogJa.select_command()
        return s
    
    def appeared(enemy):
        if Constants.LANG == Constants.LANG_EN:
            s = BattleDialogEn.appeared(enemy)
        elif Constants.LANG == Constants.LANG_JA:
            s = BattleDialogJa.appeared(enemy)
        return s

    def attacked(player, enemy, damage):
        if Constants.LANG == Constants.LANG_EN:
            s = BattleDialogEn.attacked(player, enemy, damage)
        elif Constants.LANG == Constants.LANG_JA:
            s = BattleDialogJa.attacked(player, enemy, damage)
        return s

    def spelled(player, enemy, spell, damage):
        if Constants.LANG == Constants.LANG_EN:
            s = BattleDialogEn.spelled(player, enemy, spell, damage)
        elif Constants.LANG == Constants.LANG_JA:
            s = BattleDialogJa.spelled(player, enemy, spell, damage)
        return s
    
    def not_enough_mp():
        if Constants.LANG == Constants.LANG_EN:
            s = BattleDialogEn.not_enough_mp()
        elif Constants.LANG == Constants.LANG_JA:
            s = BattleDialogJa.not_enough_mp()
        return s

    def guarding(character):
        if Constants.LANG == Constants.LANG_EN:
            s = BattleDialogEn.guarding(character)
        elif Constants.LANG == Constants.LANG_JA:
            s = BattleDialogJa.guarding(character)
        return s
    
    def defeated(enemy):
        if Constants.LANG == Constants.LANG_EN:
            s = BattleDialogEn.defeated(enemy)
        elif Constants.LANG == Constants.LANG_JA:
            s = BattleDialogJa.defeated(enemy)
        return s
    
    def died(player):
        if Constants.LANG == Constants.LANG_EN:
            s = BattleDialogEn.died(player)
        elif Constants.LANG == Constants.LANG_JA:
            s = BattleDialogJa.died(player)
        return s
    
    def escaped():
        if Constants.LANG == Constants.LANG_EN:
            s = BattleDialogEn.escaped()
        elif Constants.LANG == Constants.LANG_JA:
            s = BattleDialogJa.escaped()
        return s
    
from constants.constants import Constants
from scripts.dialog.ja.dialog_ja import Dialog

class BattleDialog(Dialog):
    def __init__(self):
        super().__init__()
    
    def command():
        s = 'たたかう: (1)' + Constants.BR
        s += 'まほう　: (2)' + Constants.BR
        s += 'ぼうぎょ: (3)' + Constants.BR
        s += 'にげる　: (4)'

        s = BattleDialog.word_in_asterisk(s)
        return s
    
    def select_command():
        s = 'どうする？: '
        return s
    
    def appeared(enemy):
        s = str(enemy.get_name()) + 'があらわれた！'

        s = BattleDialog.word_in_asterisk(s)
        return s

    def attacked(attacker, taker, damage):
        s = str(attacker.get_name()) + 'のこうげき！' + Constants.BR
        s += str(taker.get_name()) + 'は' + str(damage) + 'ダメージをうけた！'

        s = BattleDialog.word_in_asterisk(s)
        return s

    def spelled(attacker, taker, spell, damage):
        s = str(attacker.get_name()) + 'は' + str(spell.get_name()) + 'をとなえた！' + Constants.BR
        s += str(taker.get_name()) + 'は' + str(damage) + 'ダメージをうけた！'

        s = BattleDialog.word_in_asterisk(s)
        return s

    def not_enough_mp():
        s = 'MPがたりない！！' + Constants.BR

        s = BattleDialog.word_in_asterisk(s)
        return s

    def guarding(character):
        s = str(character.get_name()) + 'はみをまもっている。'

        s = BattleDialog.word_in_asterisk(s)
        return s

    def defeated(enemy):
        s = str(enemy.get_name()) + 'をたおした！'

        s = BattleDialog.word_in_asterisk(s)
        return s
    
    def died(player):
        s = str(player.get_name()) + 'はちからつきた。'

        s = BattleDialog.word_in_asterisk(s)
        return s
    
    def escaped():
        s = 'にげきれた！'

        s = BattleDialog.word_in_asterisk(s)
        return s
from constants.constants import Constants
from scripts.dialog.dialog import Dialog

class BattleDialog(Dialog):
    def __init__(self):
        super().__init__()
    
    def command():
        s = 'ATTACK: (1)' + Constants.BR
        s += 'SPELL : (2)' + Constants.BR
        s += 'GUARD : (3)' + Constants.BR
        s += 'RUN   : (4)'

        s = BattleDialog.word_in_asterisk(s)
        return s
    
    def select_command():
        s = 'Command?: '
        return s

    def appeared(enemy):
        s = str(enemy.get_name()) + ' appeared!!'

        s = BattleDialog.word_in_asterisk(s)
        return s

    def attacked(player, enemy, damage):
        s = str(player.get_name()) + "'s attack!!" + Constants.BR
        s += str(enemy.get_name()) + ' takes ' + str(damage) + ' damage!!'

        s = BattleDialog.word_in_asterisk(s)
        return s

    def spelled(player, enemy, spell, damage):
        s = str(player.get_name()) + ' spelled ' + str(spell.get_name()) + '!!' + Constants.BR
        s += str(enemy.get_name()) + ' takes ' + str(damage) + ' damage!!'

        s = BattleDialog.word_in_asterisk(s)
        return s

    def not_enough_mp():
        s = 'Not enough MP!!' + Constants.BR

        s = BattleDialog.word_in_asterisk(s)
        return s

    def guarding(character):
        s = str(character.get_name()) + ' is guarding oneself'

        s = BattleDialog.word_in_asterisk(s)
        return s

    def defeated(enemy):
        s = 'Defeated ' + str(enemy.get_name()) + '!!'

        s = BattleDialog.word_in_asterisk(s)
        return s

    def died(player):
        s = str(player.get_name()) + ' died.'

        s = BattleDialog.word_in_asterisk(s)
        return s
    
    def escaped():
        s = 'Escaped!!'

        s = BattleDialog.word_in_asterisk(s)
        return s
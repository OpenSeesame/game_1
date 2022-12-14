import time
from scripts.constants.constants import Constants
from scripts.equipment.weapon import Weapon
from scripts.equipment.armor import Armor
from scripts.equipment.shield import Shield

class Dialog():
    ASTERISK_LINE = Constants.ASTERISK * Constants.ASTERISK_COUNT + Constants.BR

    def __init__(self):
        self
    
    def word_in_asterisk(word, align=Constants.ALIGN_L):
        word_split = word.split(Constants.BR)
        s = Constants.BLANK

        for w in word_split:
            # if w is BLANK
            if len(w) == 0:
                s+= Dialog.ASTERISK_LINE
                continue

            # if w is longer than ASTERISK_COUNT
            if len(w) >= Constants.ASTERISK_COUNT:
                s+= w + Constants.BR
                continue
            
            # if align center
            if align == Constants.ALIGN_C:
                if len(word) % 2 == 0:
                    s += Constants.ASTERISK * Constants.half_count(len(w)) + ' ' + w + ' ' + Constants.ASTERISK * Constants.half_count(len(w)) + Constants.BR
                else:
                    s += Constants.ASTERISK * Constants.half_count(len(w)) + ' ' + w + ' ' + Constants.ASTERISK * (Constants.half_count(len(w)) + 1) + Constants.BR

            # if align left
            elif align == Constants.ALIGN_L:
                s += Constants.ASTERISK * Constants.ALIGN_PAD + ' ' + w + ' ' + Constants.ASTERISK * (Constants.ASTERISK_COUNT - len(w) - Constants.ALIGN_PAD - 2) + Constants.BR

            # if align right
            elif align == Constants.ALIGN_R:
                s += Constants.ASTERISK * (Constants.ASTERISK_COUNT - len(w) - Constants.ALIGN_PAD - 2) + ' ' + w + ' ' + Constants.ASTERISK * Constants.ALIGN_PAD + Constants.BR

        return s

    
    # display title
    def title():
        s = Dialog.ASTERISK_LINE
        s += Dialog.ASTERISK_LINE
        s += Constants.TITLE + Constants.BR
        s += Dialog.ASTERISK_LINE

        s = Dialog.word_in_asterisk(s, Constants.ALIGN_C)
        return s

    def new_load():
        s = 'NEW GAME(1)' + Constants.BR
        s += 'LOAD GAME(2)'

        s = Dialog.word_in_asterisk(s, Constants.ALIGN_C)
        return s

    def select_mode():
        s = '(1:NEW/2:LOAD): '
        return s

    def whats_your_name():
        s = "What's your name?: "
        return s

    def your_name_is(name):
        s = 'Your name is '
        s += '"' + name + '"?(y/n): '
        return s
    
    def listup_save_data():
        s = ""
        for num in range(1, Constants.MAX_SAVE_DATA + 1):
            s += str(num) + ': Player' + str(num) + Constants.BR
        
        return s

    def choose_data():
        s = 'Choose the data(1/2/3): '
        return s

    def print_loading():
        s = 'LOADING...'
        s = Dialog.word_in_asterisk(s, Constants.ALIGN_R)
        print(s)
        for i in range(Constants.ASTERISK_COUNT):
            print(Constants.ASTERISK, end=Constants.BLANK)
            time.sleep(0.03)
        print()

        return s

    def type_y_or_n():
        s = 'Please Type "y" or "n"'
        return s

    # display status
    def status(character):
        s = Dialog.word_in_asterisk('STATUS', Constants.ALIGN_C)
        s += character.get_name() + Constants.BR
        s += Dialog.ASTERISK_LINE
        s += str('HP :' + str(character.get_hp()).rjust(Constants.MAX_STATUS_LENGTH)) + Constants.BR
        s += str('MP :' + str(character.get_mp()).rjust(Constants.MAX_STATUS_LENGTH)) + Constants.BR
        s += str('ATK:' + str(character.get_atk()).rjust(Constants.MAX_STATUS_LENGTH)) + Constants.BR
        s += str('AR :' + str(character.get_ar()).rjust(Constants.MAX_STATUS_LENGTH)) + Constants.BR
        s += str('MR :' + str(character.get_mr()).rjust(Constants.MAX_STATUS_LENGTH)) + Constants.BR
        s = Dialog.word_in_asterisk(s)
        return s
    
    # display equipment
    def equipment(player):
        s = Dialog.word_in_asterisk('EQUIPMENT', Constants.ALIGN_C)
        s += player.get_name() + Constants.BR
        s += Dialog.ASTERISK_LINE
        s += str('BUKI  : ' + player.get_weapon().get_name() + '(' + str(player.get_weapon().get_atk()) + ')') + Constants.BR
        s += str('TATE  : ' + player.get_shield().get_name() + '(' + str(player.get_shield().get_ar()) + ')') + Constants.BR
        s += str('YOROI : ' + player.get_armor().get_name() + '(' + str(player.get_armor().get_hp()) + ')') + Constants.BR
        s = Dialog.word_in_asterisk(s)
        return s

    def equiqqed(player, equipment):
        s = Constants.BLANK
        if isinstance(equipment, Weapon):
            s = str(player.get_name()) + ' equipped ' + str(equipment.get_name()) + '(' + str(equipment.get_atk()) + ')!!'
        if isinstance(equipment, Armor):
            s = str(player.get_name()) + ' equipped ' + str(equipment.get_name()) + '(' + str(equipment.get_hp()) + ')!!'
        if isinstance(equipment, Shield):
            s = str(player.get_name()) + ' equipped ' + str(equipment.get_name()) + '(' + str(equipment.get_ar()) + ')!!'
        
        s = Dialog.word_in_asterisk(s)
        return s
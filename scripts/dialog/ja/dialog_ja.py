import time
from utils.str_utils import StrUtils
from constants.constants import Constants
from constants.names import Names
from scripts.item.equipment.weapon import Weapon
from scripts.item.equipment.armor import Armor
from scripts.item.equipment.shield import Shield

class Dialog():
    ASTERISK_LINE = Constants.ASTERISK * Constants.ASTERISK_COUNT + Constants.BR

    def __init__(self):
        self
    
    def word_in_asterisk(word, align=Constants.ALIGN_L):
        word_split = word.split(Constants.BR)
        s = Constants.BLANK

        for w in word_split:
            # if w is BLANK
            if StrUtils.len(w) == 0:
                s+= Dialog.ASTERISK_LINE
                continue

            # if w is longer than ASTERISK_COUNT
            if StrUtils.len(w) >= Constants.ASTERISK_COUNT:
                s+= w + Constants.BR
                continue
            
            # if align center
            if align == Constants.ALIGN_C:
                if StrUtils.len(word) % 2 == 0:
                    s += Constants.ASTERISK * Constants.half_count(StrUtils.len(w)) + ' ' + w + ' ' + Constants.ASTERISK * Constants.half_count(StrUtils.len(w)) + Constants.BR
                else:
                    s += Constants.ASTERISK * Constants.half_count(StrUtils.len(w)) + ' ' + w + ' ' + Constants.ASTERISK * (Constants.half_count(StrUtils.len(w)) + 1) + Constants.BR

            # if align left
            elif align == Constants.ALIGN_L:
                s += Constants.ASTERISK * Constants.ALIGN_PAD + ' ' + w + ' ' + Constants.ASTERISK * (Constants.ASTERISK_COUNT - StrUtils.len(w) - Constants.ALIGN_PAD - 2) + Constants.BR

            # if align right
            elif align == Constants.ALIGN_R:
                s += Constants.ASTERISK * (Constants.ASTERISK_COUNT - StrUtils.len(w) - Constants.ALIGN_PAD - 2) + ' ' + w + ' ' + Constants.ASTERISK * Constants.ALIGN_PAD + Constants.BR

        return s

    ### start menu (s) ###
    # display title
    def title():
        s = Dialog.ASTERISK_LINE
        s += Dialog.ASTERISK_LINE
        s += Names.TITLE + Constants.BR
        s += Dialog.ASTERISK_LINE

        s = Dialog.word_in_asterisk(s, Constants.ALIGN_C)
        return s

    def new_load():
        s = '???????????????(1)' + Constants.BR
        s += '???????????????(2)'

        s = Dialog.word_in_asterisk(s, Constants.ALIGN_C)
        return s

    def select_mode():
        s = '(1:???????????????/2:???????????????): '
        return s

    def whats_your_name():
        s = "????????????????????????: "
        return s

    def your_name_is(name):
        s = '"' + name + '"????????????????????????(y/n): '
        return s
    
    def listup_save_data():
        s = ""
        for num in range(1, Constants.MAX_SAVE_DATA + 1):
            s += str(num) + ': ???????????????' + str(num) + Constants.BR
        
        return s

    def choose_data():
        s = '???????????????????????????(1/2/3): '
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
    ### start menu (e) ###

    # display status
    def status(character):
        s = character.get_name() + Constants.BR
        s += str('???????????? :' + str(character.get_hp()).rjust(Constants.MAX_STATUS_LENGTH)) + Constants.BR
        s += str('???????????? :' + str(character.get_mp()).rjust(Constants.MAX_STATUS_LENGTH)) + Constants.BR
        s += str('???????????? :' + str(character.get_atk()).rjust(Constants.MAX_STATUS_LENGTH)) + Constants.BR
        s += str('???????????? :' + str(character.get_ar()).rjust(Constants.MAX_STATUS_LENGTH)) + Constants.BR
        s += str('???????????? :' + str(character.get_mr()).rjust(Constants.MAX_STATUS_LENGTH))
        s = Dialog.word_in_asterisk(s)
        return s
    
    # display equipment
    def equipment(player):
        s = player.get_name() + Constants.BR
        s += str('????????? : ' + player.get_weapon().get_name() + '(' + str(player.get_weapon().get_atk()) + ')') + Constants.BR
        s += str('????????? : ' + player.get_shield().get_name() + '(' + str(player.get_shield().get_ar()) + ')') + Constants.BR
        s += str('????????? : ' + player.get_armor().get_name() + '(' + str(player.get_armor().get_hp()) + ')')
        s = Dialog.word_in_asterisk(s)
        return s

    # equipped
    def equipped(player, equipment):
        s = Constants.BLANK
        if isinstance(equipment, Weapon):
            s = str(player.get_name()) + '???' + str(equipment.get_name()) + '(' + str(equipment.get_atk()) + ')?????????????????????'
        if isinstance(equipment, Armor):
            s = str(player.get_name()) + '???' + str(equipment.get_name()) + '(' + str(equipment.get_hp()) + ')?????????????????????'
        if isinstance(equipment, Shield):
            s = str(player.get_name()) + '???' + str(equipment.get_name()) + '(' + str(equipment.get_ar()) + ')?????????????????????'
        
        s = Dialog.word_in_asterisk(s)
        return s

    # unequipped
    def unequipped(player, equipment):
        s = Constants.BLANK
        if isinstance(equipment, Weapon):
            s = str(player.get_name()) + '???' + str(equipment.get_name()) + '(' + str(equipment.get_atk()) + ')???????????????'
        if isinstance(equipment, Armor):
            s = str(player.get_name()) + '???' + str(equipment.get_name()) + '(' + str(equipment.get_hp()) + ')???????????????'
        if isinstance(equipment, Shield):
            s = str(player.get_name()) + '???' + str(equipment.get_name()) + '(' + str(equipment.get_ar()) + ')???????????????'
        
        s = Dialog.word_in_asterisk(s)
        return s
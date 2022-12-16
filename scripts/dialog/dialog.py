import time
from constants.constants import Constants
from scripts.item.equipment.weapon import Weapon
from scripts.item.equipment.armor import Armor
from scripts.item.equipment.shield import Shield
from scripts.dialog.en.dialog_en import Dialog as DialogEn
from scripts.dialog.ja.dialog_ja import Dialog as DialogJa

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

    ### start menu (s) ###
    # display title
    def title():
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.title()
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.title()
        return s

    def new_load():
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.new_load()
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.new_load()
        return s

    def select_mode():
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.select_mode()
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.select_mode()
        return s

    def whats_your_name():
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.whats_your_name()
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.whats_your_name()
        return s

    def your_name_is(name):
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.your_name_is(name)
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.your_name_is(name)
        return s
    
    def listup_save_data():
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.listup_save_data()
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.listup_save_data()
        return s

    def choose_data():
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.choose_data()
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.choose_data()
        return s

    def print_loading():
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.print_loading()
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.print_loading()
        return s
    ### start menu (e) ###

    # display status
    def status(character):
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.status(character)
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.status(character)
        return s
    
    # display equipment
    def equipment(player):
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.equipment(player)
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.equipment(player)
        return s

    # equipped
    def equipped(player, equipment):
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.equipped(player, equipment)
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.equipped(player, equipment)
        return s
        return s

    # unequipped
    def unequipped(player, equipment):
        if Constants.LANG == Constants.LANG_EN:
            s = DialogEn.unequipped(player, equipment)
        elif Constants.LANG == Constants.LANG_JA:
            s = DialogJa.unequipped(player, equipment)
        return s
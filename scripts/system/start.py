from constants.constants import Constants
from scripts.dialog.dialog import Dialog
from scripts.character.player import Player

class Start:
    def __init__(self, player=Player()):
        # display title
        print(Dialog.title())

        # start game
        Start.start_game(player)
    
    
    def start_game(player):
        new_load = Start.__select_game()
        if new_load == Constants.NEW:
            Start.__new_game(player)
        elif new_load == Constants.LOAD:
            Start.__load_game(player)

    def __select_game():
        # display NEW or LOAD
        print(Dialog.new_load())

        # select NEW or LOAD
        while True:
            new_load = input(Dialog.select_mode())
            if new_load in (Constants.NEW, Constants.LOAD):
                break
        return new_load

    def __new_game(player):
        while True:
            # what's your name?
            name = input(Dialog.whats_your_name())

            while True:
                # your name is "xxx"?(y/n)
                yes_no = input(Dialog.your_name_is(name))
                if yes_no in (Constants.YES, Constants.NO):
                    break
            
            # if yes
            if yes_no == Constants.YES:
                # set name
                player.set_name(name)
                break

    def __load_game(player):
        print(Dialog.listup_save_data())
        while True:
            # choose the data
            str_i = input(Dialog.choose_data())

            # if i is not number
            if not str_i.isdecimal():
                continue

            # if i is in MAX_SAVE_DATA
            i = int(str_i)
            if i in range(1, Constants.MAX_SAVE_DATA+1):
                # load data
                Start.__load_data(player, i)
                break
    
    def __load_data(player, i):

        player.set_name('King')
        player.set_hp(3200)
        player.set_mp(320)
        player.set_atk(150)
        player.set_ar(100)
        player.set_mr(100)
        Dialog.print_loading()
 
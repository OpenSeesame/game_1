import time
from constants.constants import Constants
from scripts.character.player import Player
from scripts.character.enemy import Enemy
from scripts.dialog.battle_dialog import BattleDialog

class Battle():
    Player = Player()
    Enemy = Enemy()
    BattleEnd = False
    def __init__(self, player=Player, enemy=Enemy):

        # appeared!!
        print(BattleDialog.appeared(enemy))
        time.sleep(Constants.BATTLE_SPEED)

        # display status
        print(BattleDialog.status(player))
        time.sleep(Constants.BATTLE_SPEED)

        # turn start
        while True:
            # unguard
            player.unguard()

            # player's turn
            command = Battle.__select_command()
            Battle.__act_comand(command, player, enemy)
            if Battle.BattleEnd:
                break

            # enemy's turn
            Battle.__act_enemy(enemy, player)
            if Battle.BattleEnd:
                break

            # display status
            print(BattleDialog.status(player))
            time.sleep(Constants.BATTLE_SPEED)

    def __select_command():
        print(BattleDialog.command())
        time.sleep(Constants.BATTLE_SPEED)

        while True:
            command = input(BattleDialog.select_command())
            if command in (Constants.ATTACK, Constants.MAGIC, Constants.GUARD, Constants.RUN): 
                break
        
        return command

    def __act_comand(command, player, enemy):
        # attack
        if command == Constants.ATTACK:
            player.attack_with_dialog(enemy)
            time.sleep(Constants.BATTLE_SPEED)
        # magic
        elif command == Constants.MAGIC:
            0
        # guard
        elif command == Constants.GUARD:
            player.guard_with_dialog()
            time.sleep(Constants.BATTLE_SPEED)
        # run
        elif command == Constants.RUN:
            print(BattleDialog.escaped())
            Battle.BattleEnd = True
            time.sleep(Constants.BATTLE_SPEED)

        # check battle end
        Battle.__check_battle_end(player, enemy)

    def __act_enemy(enemy, player):
        # attack
        enemy.attack_with_dialog(player)
        time.sleep(Constants.BATTLE_SPEED)

        # check battle end
        Battle.__check_battle_end(player, enemy)

    def __check_battle_end(player, enemy):
        # game over
        if Battle.__player_is_dead(player):
            print(BattleDialog.died(player))
            Battle.BattleEnd = True

        # defeat enemy
        if Battle.__enemy_is_dead(enemy):
            print(BattleDialog.defeated(enemy))
            Battle.BattleEnd = True

    def __player_is_dead(player):
        player_is_dead = False
        if player.get_hp() == Constants.INT_ZERO:
            player_is_dead = True
        
        return player_is_dead

   
    def __enemy_is_dead(enemy):
        enemy_is_dead = False
        if enemy.get_hp() == Constants.INT_ZERO:
            enemy_is_dead = True
        
        return enemy_is_dead


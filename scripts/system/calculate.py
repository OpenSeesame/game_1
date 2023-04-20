import random
import math
from constants.constants import Constants

class Calculate:
    def __init__(self):
        self

    def calc_damage_ar(dealer, taker):
        if taker.is_guarding():
            damage = round((dealer.get_atk() * 100 / (100 + taker.get_ar() + Constants.GUARD_AR)) * random.uniform(Constants.MIN_DAMAGE_RATE, Constants.MAX_DAMAGE_RATE))
        
        else:
            damage = round((dealer.get_atk() * 100 / (100 + taker.get_ar())) * random.uniform(Constants.MIN_DAMAGE_RATE, Constants.MAX_DAMAGE_RATE))

        return damage

    def calc_damage_mr(dealer, taker, spell):
        if taker.is_guarding():
            damage = round(((dealer.get_atk() + spell.get_additional_damage()) * 100 / (100 + taker.get_mr() + Constants.GUARD_MR)) * random.uniform(Constants.MIN_DAMAGE_RATE, Constants.MAX_DAMAGE_RATE))
        
        else:
            damage = round(((dealer.get_atk() + spell.get_additional_damage()) * 100 / (100 + taker.get_mr())) * random.uniform(Constants.MIN_DAMAGE_RATE, Constants.MAX_DAMAGE_RATE))

        return damage
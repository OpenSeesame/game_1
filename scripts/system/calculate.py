import random
import math
from constants.constants import Constants

class Calculate:
    def __init__(self):
        self

    def calc_damage_ar(dealer, taker):
        if taker.is_guarding():
            damage = round((dealer.get_atk() * 100 / (100 + taker.get_ar() + Constants.GUARD_AR)) * random.uniform(0.9, 1.1))
        
        else:
            damage = round((dealer.get_atk() * 100 / (100 + taker.get_ar())) * random.uniform(0.9, 1.1))

        return damage

    def calc_damage_mr(dealer, taker):
        if taker.is_guarding():
            damage = round((dealer.get_atk() * 100 / (100 + taker.get_mr() + Constants.GUARD_MR)) * random.uniform(0.9, 1.1))
        
        else:
            damage = round((dealer.get_atk() * 100 / (100 + taker.get_mr())) * random.uniform(0.9, 1.1))

        return damage
import random
import math

class Calculate:
    def __init__(self):
        self

    def calc_damage(atk, resist):
        damage = round((atk * 100 / (100 + resist)) * random.uniform(0.9, 1.1))
        return damage
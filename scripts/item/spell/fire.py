from scripts.item.spell.spell import Spell
from constants.names import Names

class Fire(Spell):
    Name=Names.FIRE
    AdditionalDamage=5
    ConsMp=10

    def __init__(self, name=Name, cons_mp=ConsMp, additional_damage=AdditionalDamage):
        super().__init__(name, cons_mp, additional_damage)
from scripts.character.enemy import Enemy
from constants.names import Names

class Slime(Enemy):
    Name = Names.SLIME
    Hp = 100
    Mp = 50
    Atk = 25
    Ar = 10
    Mr = 0

    def __init__(self, name=Name, hp=Hp, mp=Mp, atk=Atk, ar=Ar, mr=Mr):
        super().__init__(name, hp, mp, atk, ar, mr)

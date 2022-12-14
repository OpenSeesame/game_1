from scripts.character.enemy import Enemy

class Slime(Enemy):
    Hp = 100
    Mp = 50
    Atk = 25
    Ar = 10
    Mr = 0

    def __init__(self, name='Slime', hp=Hp, mp=Mp, atk=Atk, ar=Ar, mr=Mr):
        super().__init__(name, hp, mp, atk, ar, mr)

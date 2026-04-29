# pokemon.py creates a Pokemon class    

class Pokemon:
    def __init__(self, pid, name, type1, type2, hp, atk, defense, sp_atk, sp_def, speed):
        self.id = pid
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = int(hp)
        self.attack = int(atk)
        self.defense = int(defense)
        self.sp_atk = int(sp_atk)
        self.sp_def = int(sp_def)
        self.speed = int(speed)
        self.ability = ""
        self.item = ""
        self.moves[4] = []

    def __repr__(self):
        return f"{self.name} ({self.type1}/{self.type2})"
# pokemon.py creates a Pokemon class    
from models.packager import POKEDEX, MOVESETS


class Pokemon:
    def __init__(self, name):
        """
        Creates a Pokemon object by pulling data from packager.
        """
        self.name = name

        base = POKEDEX.get(name)
        if not base:
            raise ValueError(f"Pokemon '{name}' not found in POKEDEX")

        # Core stats pulled from dictionary-backed object
        self.id = base.id
        self.type1 = base.type1
        self.type2 = base.type2
        self.hp = base.hp
        self.attack = base.attack
        self.defense = base.defense
        self.sp_atk = base.sp_atk
        self.sp_def = base.sp_def
        self.speed = base.speed

        # Moveset pulled from MOVESETS (fallback to empty list)

        # !! Update to be 4 moveslots versus moveset
        self.moves = MOVESETS.get(name, [])

    def get_moves(self):
        """Returns full moveset"""
        return self.moves

    def get_stats(self):
        """Returns stats as a dictionary (useful for UI/API)"""
        return {
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "sp_atk": self.sp_atk,
            "sp_def": self.sp_def,
            "speed": self.speed,
        }

    def __repr__(self):
        return f"{self.name} ({self.type1}/{self.type2})"
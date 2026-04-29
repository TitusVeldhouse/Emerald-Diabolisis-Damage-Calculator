from pkmnDict import POKEDEX, load_pokemon

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_pokemon(self, pokemon):
        if len(self.members) >= 6:
            raise Exception("Team already has 6 Pokémon!")
        self.members.append(pokemon)

    def remove_pokemon(self, pkmn):
        self.members.remove(pkmn)

    def overwrite_pokemon(self, oldPkmn, newPkmn):
        self.remove_pokemon(oldPkmn)
        self.add_pokemon(newPkmn)

    def list_team(self):
        return self.members
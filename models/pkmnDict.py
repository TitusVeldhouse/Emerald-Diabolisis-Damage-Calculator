import csv
from pokemon import Pokemon

POKEDEX = []

def load_pokemon(filename="pokemon.csv"):
    global POKEDEX
    POKEDEX = []

    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            POKEDEX.append(Pokemon(*row))

    return POKEDEX


def get_pokemon_by_id(pid):
    for p in POKEDEX:
        if p.id == pid:
            return p
    return None
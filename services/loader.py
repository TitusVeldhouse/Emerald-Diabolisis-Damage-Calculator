import csv
import json
from models.pokemon import Pokemon

def load_pokemon(filename="data/pokemon.csv"):
    pokedex = {}

    with open(filename, newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            p = Pokemon(*row)
            pokedex[p.name] = p

    return pokedex


def load_movesets(filename="data/movesets.json"):
    with open(filename) as f:
        return json.load(f)
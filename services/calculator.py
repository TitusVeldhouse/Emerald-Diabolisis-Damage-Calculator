from models.packager import ITEMS, MOVES
from models.pokemon import Pokemon

physTypes = ["Normal", "Fighting", "Ghost", "Ground", "Rock", "Steel", "Flying"]

def is_Physical(pkmnData):
    type = MOVES.type
    for check in physTypes:
        if type = check:
            return ("attack", "defense")
    return ("spAtk", "spDef")

def calculate(currPkmn, oppPkmn):

    # Check if move can do damage
    if(MOVES.cat = 1):

        # Get move and pokemon data
        pkmnData = currPkmn.get_stats()
        isPhys = is_Physical(pkmnData)
        oppHP = oppPkmn.get_stats("hp")

        # Calculate Damage
        damage = (((((2 *  pkmnData.level / 5 + 2) * is_Physical(pkmnData) ) / 50) + 2) * Modifier)
        return (damage, damage / 0.85)
    
    # Return no damage
    return (0, 0)
    

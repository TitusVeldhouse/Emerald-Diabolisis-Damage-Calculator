# Uncomment when implemented
# from models.packager import ITEMS

class Item:
    def __init__(self, name):
        """
        Creates an Item object by pulling data from packager.
        """
        self.name = name

        # !! Uncomment when implemented

        """
        base = ITEMS.get(name)
        if not base:
            raise ValueError(f"Pokemon '{name}' not found in POKEDEX")
        

        # Core stats pulled from dictionary-backed object
        self.boost = base.boost (or mult?)
        self.reqs = base.id
        """
class Inventory:
    def __init__(self, gold=0, items=[]):
        """_summary_

        Args:
            gold (int, optional): _description_. Defaults to 0.
            items (list, optional): _description_. Defaults to [].
        """        
        self.gold = gold
        self.items = items

    def transfer(self, reciever):
        reciever.gold += self.gold
        self.gold = 0
        reciever.items += self.items
        self.items = []
    
    def get_obj(self):
        return self.__dict__

class Character(Inventory):
    def __init__(self, name, race, gold=0, items=[]):
        self.name = name
        self.race = race
        super().__init__(gold, items)

class Chest(Inventory):
    def __init__(self, items=[], gold=0, locked=False):
        super().__init__(gold, items)
        self.locked = locked

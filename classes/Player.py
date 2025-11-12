from classes.GameObject import GameObject
from classes.Inventory import Inventory
from pgzero.actor import Actor

class Player(GameObject):
    def __init__(self):
        super().__init__(Actor("front_unfocused"))
        self.health = 100
        self.inventory = Inventory()
        #TODO add spells    
        self.spells = []
    
    def draw(self, screen) -> None:
        self.target.draw()
    
    def update(self, pos, button=None) -> None:
        #TODO
        pass
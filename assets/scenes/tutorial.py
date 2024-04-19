from ursina import *
from assets.scripts.terrain import Terrain
from assets.scripts.chest import Chest
from assets.scripts.scool import Scool
from random import randint

class Tutorial():
    def __init__(self):
        super().__init__()
        self.chest = Chest(position=0)
        self.chest = Chest(position=3)
        self.chest = Chest(position=6)
        self.terrain = Terrain(scale=(100, 1, 100))
        self.scool = Scool()
        self.scool.rotation = (0,180,0)
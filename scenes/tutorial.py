from ursina import *
from scripts.terrain import Terrain
from scripts.chest import Chest
from scripts.scool import Scool
from scripts.player import Player
from random import randint
class Tutorial(Entity):
    def __init__(self):
        super().__init__()
        self.sky = Sky() 
        self.chests = range(3)
        self.player = Player()
        self.player.collider = BoxCollider(self.player, center=Vec3(0,0,0), size=Vec3(3,2,3))
        self.chests = [Chest(position=i*3, chosed=i ) for i in range(5)]
        self.random_chest = randint(0, len(self.chests))
        self.terrain = Terrain(scale=(100, 1, 100))
    def input(self, key):
        if key == 'left mouse down':
            self.hit_info = raycast(camera.world_position, camera.forward, distance=2)
            for self.chest in self.chests:
                if (mouse.hovered_entity == self.chest):
                    if (self.chest.chosed == self.random_chest):
                        self.text = Text("PARABÉNS, VOCÊ <green>ACERTOU",origin=(0,-2), scale=(2,2))                

                
 
        
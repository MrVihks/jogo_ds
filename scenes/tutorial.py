from ursina import *
from scripts.terrain import Terrain
from scripts.chest import Chest
from scripts.scool import Scool
from scripts.scool_ import ScoolTwo
from scripts.player import Player
from scripts.tree import Tree

from random import randint

class Tutorial(Entity):
    def __init__(self, dificult):
        super().__init__()
        self.hint_text = ""
        scene.fog_density = (50, 200)
        self.new_dificult = dificult
        self.sky = Sky() 
        self.chests = range(3)
        self.player = Player()
        self.player.collider = BoxCollider(self.player, center=Vec3(0,0,0), size=Vec3(3,2,3))
        self.scool = Scool(position=(3,0,5), scale=(0.5)) 
        self.scool.rotation_y = (180)
        self.chests = [Chest(position=i*3, chosed=i ) for i in range(dificult)]
        self.trees = [Tree(position=(randint(-27, 27),0,randint(-27, 27))) for i in range(35)]
        self.random_chest = randint(0, len(self.chests))
        self.terrain = Terrain(scale=(100, 1, 100))
        self.hint = Text("Escolha o baú correto", origin=(2,14), scale=(1.2,1.2))
        self.hint.create_background(color=color.red) 
    def update(self):
        self.scool.rotation_y = self.player.rotation_y + 180
    def input(self, key):
        for self.chest in self.chests:
            if (mouse.hovered_entity == self.chest):
                mouse.hovered_entity.color = color.green
            else:
                self.chest.color = color.rgba(1,1,1,1)
        if key == 'left mouse down':
            self.hit_info = raycast(camera.world_position, camera.forward, distance=2) 
            for self.chest in self.chests:
                if (mouse.hovered_entity == self.chest):
                    if (self.chest.chosed == self.random_chest):
                        scene.clear()
                        self.text = Text("PARABÉNS, VOCÊ <green>ACERTOU",origin=(0,-2), scale=(2,2))     
                        self.again = Button(text='PRÓXIMA FASE', color=color.azure, scale=(0.3, 0.1, 0), position=(0, 0))
                        self.again.on_click = self.next_stage
                    else:
                        scene.clear()
                        self.textError = Text("VOCÊ <red>ERROU :(",origin=(0,-2), scale=(2,2))  
                        self.losed = Button(text='JOGAR NOVAMENTE', color=color.red, scale=(0.3, 0.1, 0), position=(0, 0))
                        self.losed.on_click = self.start_again
    def start_again(self):
        scene.clear()
        Tutorial(2)
    def next_stage(self):
        self.new_dificult = self.new_dificult + 2
        self.stage = 0
        for self.i in range(0, self.new_dificult, 2):
            self.stage = self.stage + 1
        scene.clear()
        Tutorial(self.new_dificult)
        self.hint = Text(text="FASE "+ str(self.stage), origin=(-8,14), scale=(1.2,1.2))
        self.hint.create_background(color=color.blue) 
                          
                               

                
 
        
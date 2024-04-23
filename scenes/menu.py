from ursina import *
from scripts.scool import Scool
from scenes.tutorial_texts import TutorialTexts

class Menu(Entity):
    def __init__(self):
        super().__init__()
        self.text = Text(text="JOGO DA ADIVINHAÇÃO",origin=(0,-3), scale=(2,2))
        self.start = Button(text='INICIAR', color=color.azure, scale=(0.3, 0.1, 0), position=(0, 0))
        self.exit = Button(text='SAIR', color=color.red, scale=(0.3, 0.1, 0), origin=(0,1.2))
        self.exit.text_size=2.3
        self.start.text_size=2.3
        self.scool1 = Scool(position=(-3.5,-3,0), scale=(0.3))
        self.scool2 = Scool(position=(3.5,-3,0), scale=(0.3))
        self.exit.on_click = self.exit_game
        self.start.on_click = self.go_to_next
        self.destroy_all = False
    def update(self):
        if(self.destroy_all != True):
            self.scool1.rotation_y -= time.dt * 150
            self.scool2.rotation_y += time.dt * 150
         
    def go_to_next(self):
        self.destroy_all = True
        scene.clear()
        self.tutorial = TutorialTexts()
       
    def exit_game(self):
        application.quit()
    

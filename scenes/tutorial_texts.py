from ursina import *
from scripts.scool import Scool
from scenes.tutorial import Tutorial
class TutorialTexts():
    def __init__(self):
        super().__init__()
        self.text1 = Text(text="BEM VINDO AO <red>TUTORIAL <default>:)",origin=(0,-2), scale=(2,2))
        self.text2 = Text("ESTE É O JOGO DA ADVINHAÇÃO,\n VOCÊ PRECISA ESCOLHER O BAÚ <green>CERTO PARA PASSAR DE FASE !",origin=(0,0), scale=(1.5,1.5))
        self.start = Button(text='COMEÇAR', color=color.green, scale=(0.3, 0.1, 0), origin=(0,1.5))
        self.start.text_size=2.3 
        self.start.on_click = self.go_to_next
    def go_to_next(self):
        destroy(self.text1) 
        destroy(self.text2)            
        destroy(self.start)
        self.tutorial = Tutorial(2)  
            
from ursina import *
from scenes.menu import Menu

app = Ursina(title="Jogo DS", size=(1280, 720))

Menu()

app.run()
from ursina import *

app = Ursina(title="Falai vinao")

player = Entity(model="cube", color=color.orange, scale_y=2)

def update():
    player.x += held_keys["d"] * time.dt
    player.x -= held_keys["a"] * time.dt

app.run()
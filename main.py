from ursina import *
from assets.scenes.tutorial import Tutorial
from assets.scripts.player import Player
from assets.scripts.chest import Chest
from ursina.shaders import lit_with_shadows_shader

app = Ursina(title="Jogo DS", size=(1280, 720))

sky = Sky()     

player = Player()
player.collider = BoxCollider(player, center=Vec3(0,0,0), size=Vec3(2,2,2))

tutorial = Tutorial()
Entity.default_shader = lit_with_shadows_shader

app.run()
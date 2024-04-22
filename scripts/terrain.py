from ursina import *

class Terrain(Entity):
    def __init__(self, scale):
        super().__init__(
            model="plane",
            texture="../textures/ground.jpg",
            scale=scale,
            position=Vec3(0,0,0),
            collider="box"
        )
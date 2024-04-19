from ursina import *

class Terrain(Entity):
    def __init__(self, scale):
        super().__init__(
            model="cube",
            texture="../textures/ground.jpg",
            scale=scale,
            position=Vec3(0,-35,1),
            collider="box"
        )

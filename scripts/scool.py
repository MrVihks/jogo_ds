from ursina import *

class Scool(Entity):
    def __init__(self, position, scale):
        super().__init__(
            model="../assets/models/scool.glb",
            scale=scale,
            position=position,
            collider="mesh"
        )
   
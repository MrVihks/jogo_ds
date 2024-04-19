from ursina import *

class Scool(Entity):
    def __init__(self):
        super().__init__(
            model="../models/scool.glb",
            scale=(0.5),
            position=(3,-34.5, 2),
            collider="mesh"
        )
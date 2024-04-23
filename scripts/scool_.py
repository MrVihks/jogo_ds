from ursina import *

class ScoolTwo(Entity):
    def __init__(self):
        super().__init__(
            model="../assets/models/scool.glb",
            texture="../assets/textures/scool_texture",
            scale=(0.5)
        )
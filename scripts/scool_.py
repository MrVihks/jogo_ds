from ursina import *

class ScoolTwo(Entity):
    def __init__(self):
        super().__init__(
            model="../assets/models/scool_.obj",
            texture="../assets/textures/scool_texture",
            scale=(0.5)
        )
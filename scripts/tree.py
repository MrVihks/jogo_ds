from ursina import *

class Tree(Entity):
    def __init__(self, position):
        super().__init__(
            model="../assets/models/tree.glb",
            scale=(0.15),
            position=position
        )
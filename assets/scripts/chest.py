from ursina import *

class Chest(Entity):
    def __init__(self, position):
        super().__init__(
            model="../models/chest.glb",
            scale=(0.4),
            position=Vec3(position,-34.5,0),
            collider="mesh"
        )
        

from ursina import *

class Chest(Entity):
    def __init__(self, position, chosed):
        super().__init__(
            model="../assets/models/chest.glb",
            scale=(0.4),
            position=Vec3(position,0,3),
            collider="box",
            __name__=chosed
        )
        self.chosed = chosed
        

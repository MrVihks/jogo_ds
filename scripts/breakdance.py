from ursina import * 

class BreakDance(Entity):
    def __init__(self, position, scale):
         super().__init__(
            model="../assets/models/breakdance.glb",
            scale=scale,
            position=position,
            collider="mesh"
        )
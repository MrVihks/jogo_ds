from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            collider="mesh",
            scale=(1),
            position=Vec3(5.86158, 0.00100005, -9.17894),
            speed=12
        )
        

        
                
        
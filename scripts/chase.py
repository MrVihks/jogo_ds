from ursina import *
from scripts.scool import Scool
from scripts.player import Player

class Chaser():
    def __init__(self, scool, player, speed = 1.1, offset: tuple = (0, 0, 0)): # vou tipar sim testone
        self.player = player
        self.scool = scool
        self.speed = speed

    def check_collision(self):
        col = self.player.intersects(self.scool)

        if(col.hit):
            return True
        else:
            return False

    def walk_to(self):
        self.scool.add_script(SmoothFollow(target=self.player, offset=(0, 0, 0), speed=self.speed))

import pygame
from pygame.locals import *
import Events


class CollisionHandler(object):
    pass

    @classmethod
    def is_colliding(cls, block, map):
        for i in range(0, 3):
            return block.y <= 31 or map.map[block.x][block.y+1]



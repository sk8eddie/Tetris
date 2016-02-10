import pygame
from pygame.locals import *
import Events


class CollisionHandler(object):

    @classmethod
    def is_colliding(cls, block, map):
        # for i in range(0, 3):
            return block.y >= 31 or map.map[block.x][block.y+1] or map.map[block.x+1][block.y+1] \
                   or map.map[block.x+2][block.y+1] or map.map[block.x+3][block.y+1]




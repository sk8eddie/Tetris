import pygame
from pygame.locals import *
import Events


class CollisionHandler(object):

    @classmethod
    def is_colliding(cls, block, map):
        return block.is_colliding_with_bottom() or block.is_colliding_with_map(map=map)






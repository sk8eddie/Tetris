import pygame
from pygame.locals import *
import os
import random

# Abstract class
class Block(object):

    def __init__(self):
        self.form = [[0 for x in range(20)]for x in range(32)]
        self.image = pygame.image.load(os.path.join('lib\media', 'Block.png'))
        self.map = map

    def update(self):
        pass

    def shunt_left(self):
        pass

    def shunt_right(self):
        pass

    def rotate_clockwise(self):
        pass

    def super_drop(self):
        pass

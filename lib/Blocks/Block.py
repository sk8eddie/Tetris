import pygame
from pygame.locals import *
import os
import random


class Block(object):

    def __init__(self, window_width, window_height):
        self.x = 0
        self.y = 0
        self.window_width = window_width
        self.window_height = window_height
        self.velocity = 10
        self.rotation = [0, 1, 2, 3]
        self.image = pygame.image.load(os.path.join('lib\media', 'Block.png'))

    def update(self):
        self.y += self.velocity

    def shunt_left(self):
        self.x -= self.velocity

    def shunt_right(self):
        self.x += self.velocity

    def rotate_clockwise(self):
        pass

    def super_drop(self):
        pass

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))



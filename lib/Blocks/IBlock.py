import pygame
from pygame.locals import *
import os
import random
from lib.Blocks.Block import Block


class IBlock(Block):

    def __init__(self):
        super(IBlock, self).__init__()

    def draw(self, window):
        window.blit(self.image)
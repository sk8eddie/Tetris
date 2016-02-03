import pygame
from pygame.locals import *
import os
import random
from lib.Blocks.Block import Block


class IBlock(Block):

    def __init__(self, map):
        super(IBlock, self).__init__()
        self.form = [[True, True, True, True],
                      [False, False, False, False],
                      [False, False, False, False],
                      [False, False, False, False]
                    ]
        self.map = map

    def spawn_block(self):
        for x in range(0, 20):
            for y in range(0, 32):
                if self.form[x][y]:
                    self.map,map[x][y]=True
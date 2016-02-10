import pygame
from pygame.locals import *
import os
import random
from lib.Blocks.Block import Block
from lib.EventHandler import *


class IBlock(Block):

    def __init__(self, map):
        super(IBlock, self).__init__()
        self.form = [[True, True, True, True],
                      [False, False, False, False],
                      [False, False, False, False],
                      [False, False, False, False]
                    ]
        self.map = map
        self.x = 0
        self.y = 0

    def to_map(self, map):
        for i in range(0, 3):
            map.map[self.x+i][self.y]=True

    def spawn_block(self):
        self.to_map(map=self.map)
        self.x = 0
        self.y = 0

    def move_right(self):
        self.x += 1
        self.map.map[self.x-1][self.y] = False

    def move_left(self):
        self.x -= 1
        self.map.map[self.x+1][self.y] = False

    def update(self):
        if False:
            self.draw()
        else:
            self.y += 1
            self.draw()

    def draw(self):
        for y in range(0, 31):
            for x in range(0, 19):
                if x < 4 and y < 4:
                    if self.form[y][x]:
                        self.map.map[x+self.x][y+self.y] = True
                        self.map.map[x+self.x][y+self.y-1] = False














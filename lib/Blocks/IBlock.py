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
        self.x = 9
        self.y = 0

    def to_map(self):
        if self.rotation == 1 or self.rotation == 3:
            for i in range(0, 3):
                self.map.level[self.x+i][self.y] = True
        elif self.rotation == 2 or self.rotation == 4:
            for i in range(1, 4):
                self.map.level[self.x][self.y+i] = True

    def spawn_block(self):
        self.to_map()
        if self.rotation == 2 or self.rotation == 4:
            self.rotate(clockwise=True, remove=False)
        self.x = 9
        self.y = 0

    def move_right(self):                       # TODO
        for x in range(0, 4):
            for y in range(0, 4):
                if self.form[x][y]:
                    if not self.map.level[self.x+x][self.y+y]:
                        self.x += 1
                        self.map.level[self.x-x][self.y-y] = False
        self.x -= 2

    def move_left(self):
        pass

    def update(self):
        self.y += 1
        self.draw()

    def is_colliding_with_map(self, map):
        if self.rotation == 1 or self.rotation == 3:
            check_list = []
            for x in range(0, 4):
                check_list.append(map.level[self.x+x][self.y+1])
            return any(check_list)
        elif self.rotation == 2 or self.rotation == 4:
            return map.level[self.x][self.y+4]

    def is_colliding_with_bottom(self):
        if self.rotation == 1 or self.rotation == 3:
                return self.y > 30
        elif self.rotation == 2 or self.rotation == 4:
            return self.y+4 > 31


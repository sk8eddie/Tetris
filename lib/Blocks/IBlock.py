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
        self.x = -11
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
        self.x = -11
        self.y = 0

    def move_right(self):       # Flawless ^^
        move = True
        for y in range(0, 4):
            for x in range(0, 4):
                if self.form[y][x]:
                    if self.rotation == 1 or self.rotation == 3:
                        if self.map.level[self.x+(x+1)][self.y+y+1]:
                            move = False
                    elif self.rotation == 2 or self.rotation == 4:
                        if self.map.level[self.x+x+1][self.y+y]:
                            move = False
        if move:
            self.x += 1
            start = 0
            end = 4
            if self.rotation == 1 or self.rotation == 3:
                start = 0
                end = 1
            for why in range(start, end):
                self.map.level[self.x-1][self.y+why] = False

    def move_left(self):            # Your logic is flawed :(   # TODO Bug when rotation is 2/4 :(
        move = True
        for y in range(0, 4):
            for x in range(0, 4):
                if self.form[y][x]:
                    if self.rotation == 1 or self.rotation == 3:
                        if self.map.level[self.x-1][self.y+y+1]:
                            move = False
                    elif self.rotation == 2 or self.rotation == 4:
                        if self.map.level[self.x-1][self.y+y]:
                            move = False
        if move:
            self.x -= 1
            start = 0
            end = 4
            if self.rotation == 1 or self.rotation == 3:
                start = 1
                end = 2
            for why in range(start, end):
                for eks in range(0, 5):
                    self.map.level[self.x+eks][self.y+(why-1)] = False

    def update(self):
        self.y += 1
        self.draw()

    def is_block_underneath(self, map):
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


import pygame
from pygame.locals import *
import os
import random

# Abstract class
class Block(object):

    def __init__(self):
        self.form = [[0 for x in range(4)]for x in range(4)]
        self.image = pygame.image.load(os.path.join('lib' + os.sep + 'media', 'Block.png'))
        self.rotation = 1
        self.rate = 10
        self.x = 9
        self.y = 0

    def rotate(self, clockwise, remove):
        loop_counter = 1
        if self.can_rotate():
            if clockwise:
                loop_counter = 3

            for r in range(0, loop_counter):
                temp_list1 = [[0 for x in range(4)]for x in range(4)]
                temp_list2 = [[0 for x in range(4)]for x in range(4)]

                for i in range(0, 4):
                    for j in range(0, 4):
                        temp_list1[i][j] = self.form[j][i]
                        if remove:
                            self.map.level[i+self.x][self.y+j] = False

                for e in range(0, 4):
                    temp_list2[e] = temp_list1[3-e]

                self.form = temp_list1

                self.rotation += 1
                if self.rotation > 4:
                    self.rotation = 1

    def can_rotate(self):
        rotate = True
        for y in range(0, 4):
            for x in range(0,4):
                if not self.form[y][x]:
                    if self.map.level[self.x+x][self.y+y]:
                        rotate = False
        return rotate

    def super_drop(self, rate):
        self.rate = rate

    def draw(self):
        for y in range(0, 4):
            for x in range(0, 4):
                if self.form[y][x]:
                    self.map.level[self.x+x][self.y-1] = False
                    self.map.level[self.x+x][self.y+y] = True

    def is_colliding_with_bottom(self):
        if self.rotation == 1 or self.rotation == 3:
            return self.y > 30
        elif self.rotation == 2 or self.rotation == 4:
            return self.y+4 > 31

    def update(self):
        self.y += 1
        self.draw()


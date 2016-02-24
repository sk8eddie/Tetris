import pygame
from pygame.locals import *
import os
import random

# Abstract class
class Block(object):

    def __init__(self):
        self.form = [[0 for x in range(20)]for x in range(32)]
        self.image = pygame.image.load(os.path.join('lib' + os.sep + 'media', 'Block.png'))
        self.map = map
        self.rotation = 1
        self.rate = 10

    def update(self):
        pass

    def rotate(self, clockwise, remove):
        loop_counter = 1
        if clockwise:
            loop_counter = 3

        for r in range(0, loop_counter):
            temp_list1 = [[0 for x in range(4)]for x in range(4)]
            temp_list2 = [[0 for x in range(4)]for x in range(4)]

            for i in range(0, 4):
                for j in range(0, 4):
                    temp_list1[i][j] = self.form[j][i]
                    if remove:
                        self.map.map[i+self.x][self.y-j] = False

            for e in range(0, 4):
                temp_list2[e] = temp_list1[3-e]

            self.form = temp_list1

            string = ""
            for i in range(0, 4):
                string += "\n"
                for j in range(0, 4):
                    if self.form[i][j]:
                        string += "X"
                    else:
                        string += "/"
            print(string)

            self.rotation += 1
            if self.rotation > 4:
                self.rotation = 1


    def super_drop(self, rate):
        self.rate = rate

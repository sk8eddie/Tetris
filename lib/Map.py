import pygame
from pygame.locals import *
import os
from lib.Functions import *


class Map(object):

    def __init__(self):
        self.level = []
        self.image = pygame.image.load(os.path.join('lib\media', 'Block.png'))
        for i in range(0, 20, 1):
            cell_dump = []
            for e in range(0, 37, 1):
                cell_dump.append(False)
            self.level.append(cell_dump)

    def full_row(self, block):              # TODO For some it is full when not full
        # number_of_rows = 0
        y = 0
        x = 0
        while y < 32:
            x = 0
            while x < 19:
                if self.level[x][y]:
                    x += 1
                    if x == 19:
                        x = 0
                        print("Full Y: {0}".format(y))
                        # number_of_rows += 1
                        # if number_of_rows <= 4:
                        self.drop_rows(y=y)
                else:
                    break
            y += 1

    def drop_rows(self, y):
        temp_level = self.level
        for why in range(y, 0, -1):
            for x in range(0, 20):
                self.level[x][why+1] = temp_level[x][why]

    def delete_row(self, y):
        for x in range(0, 20, 1):
            self.level[x][y] = False

    def is_cell_block_true(self, ):
        pass

    def draw(self, window):
        for x in range(0, 20):
            for y in range(0, 32):
                if self.level[x][y]:
                    window.blit(self.image, (translate_coord_to_screen(x=x, y=y)))


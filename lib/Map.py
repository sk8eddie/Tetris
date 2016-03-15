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

    def row_is_full(self, block):           # TODO
        y = 0
        x = 0
        while y < 31:
            while x < 19:
                if self.level[x][y]:
                    x += 1
                    if x == 19:
                        print("Full")
                        self.delete_row(y=y)
                else:
                    y += 1

    def delete_row(self, y):        # Works ~ish
        for x in range(0, 20, 1):
            self.level[x][y] = False

    def is_cell_block_true(self, ):
        pass

    def draw(self, window):
        for x in range(0, 20):
            for y in range(0, 32):
                if self.level[x][y]:
                    window.blit(self.image, (translate_coord_to_screen(x=x, y=y)))


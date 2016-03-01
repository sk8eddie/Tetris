import pygame
from pygame.locals import *
import os
from lib.Functions import *


class Map(object):

    def __init__(self):
        self.map = []
        self.image = pygame.image.load(os.path.join('lib\media', 'Block.png'))
        for i in range(0, 20, 1):
            cell_dump = []
            for e in range(0, 32, 1):
                cell_dump.append(False)
            self.map.append(cell_dump)

    def row_is_full(self, block):
        for x in range(20, 0, -1):
            for y in range(block.y, block.y-4, -1):
                if all(self.map[x][y]):
                    self.delete_row(block=block)

    def delete_row(self, block):  # TODO
        for x in range(20, 0, -1):
            for y in range(block.y, block.y-4, -1):
                self.map[x][y] = False

    def is_cell_block_true(self, ):
        pass

    def draw(self, window):
        for x in range(0, 20):
            for y in range(0, 32):
                if self.map[x][y]:
                    window.blit(self.image, (translate_coord_to_screen(x=x, y=y)))


import pygame
from pygame.locals import *
import sys
from lib.EventHandler import *
from lib.Blocks.IBlock import IBlock
from lib.Blocks.Block import Block
from lib.Map import Map


class Main(object):

    def __init__(self):
        self.score = 0
        self.window = pygame.display.set_mode((500, 640))
        self.clock = pygame.time.Clock()
        self.map = Map()
        self.block = IBlock(map=self.map)

        while True:
            self.update()
            self.draw()
            self.clock.tick(10)

    def update(self):
        Eventhandler.handle_events()
        self.block.update()

    def draw(self):
        self.window.fill((0, 0, 255))
        self.block.spawn_block()

        pygame.display.flip()

main = Main()

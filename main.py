import pygame
from pygame.locals import *
import sys
from lib.EventHandler import *
from lib.Blocks.IBlock import IBlock
from lib.Blocks.Block import Block
from lib.Map import Map
from lib.CollisionHandler import *


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
            self.clock.tick(self.block.rate)
            if CollisionHandler.is_colliding(block=self.block, map=self.map):
                self.block.spawn_block()
            self.block.super_drop(10)

    def update(self):
        EventHandler.handle_events(block=self.block)
        if self.block.y < 31:
            self.block.update()

    def draw(self):
        self.window.fill((0, 0, 255))
        self.map.draw(window=self.window)

        pygame.display.flip()

main = Main()

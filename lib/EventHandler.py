import pygame
from pygame.locals import *
import sys
import Events


class Eventhandler(object):

    @classmethod
    def handle_events(cls, block):
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    block.move_left()
                elif event.key == K_RIGHT:
                    block.move_right()
                elif event.key == K_UP:
                    block.rotate(clockwise=False, remove=True)
                elif event.key == K_DOWN:
                    if block.rate == 10:
                        block.super_drop(10000)
                    else:
                        block.super_drop(10)
                elif event.key == K_ESCAPE:
                    quit()
                    sys.exit()

    # @classmethod
    # def is_action(cls):
    #     for event in pygame.event.get():
    #         return event.type == KEYDOWN and event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP


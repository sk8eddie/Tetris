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
                    pass
                elif event.key == K_RIGHT:
                    block.move_right()
                elif event.key == K_UP:
                    pass
                elif event.key == K_ESCAPE:
                    quit()
                    sys.exit()

    # @classmethod
    # def is_action(cls):
    #     for event in pygame.event.get():
    #         return event.type == KEYDOWN and event.key ==K_LEFT or event.key == K_RIGHT or event.key == K_UP


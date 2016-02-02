import pygame
from pygame.locals import *
import sys
import Events


class Eventhandler(object):

    @classmethod
    def handle_events(cls):
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pass
                elif event.key == K_RIGHT:
                    pass
                elif event.key == K_ESCAPE:
                    quit()
                    sys.exit()
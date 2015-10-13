# from math import hypot

import pygame as pg


class Line(object):
    """Line class to show the map distance"""
    def __init__(self, start):
        self.start = start
        self.end = start
        self.color = (255, 212, 123)
        self.moving = True

    def set_end(self, pos):
        self.end = pos
        self.moving = False

    def draw(self, surface):
        pg.draw.line(surface, self.color, self.start, self.end, 3)

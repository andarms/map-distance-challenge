from math import sqrt
from random import randint

import pygame as pg


class Line(object):
    """Line class to show the map distance"""
    def __init__(self, start):
        self.start = start
        self.end = start
        self.point_color = [randint(0, 255) for _ in range(3)]
        self.moving = True

    def update(self):
        self.distance = self.calculate_distance()
        lerp_val = get_lerp_val(self.distance)
        self.color = lerp(pg.Color('cyan'), pg.Color('orange'), lerp_val)

    def draw(self, surface):
        pg.draw.line(surface, self.color, self.start, self.end, 3)
        pg.draw.circle(surface, self.point_color, self.start, 3)
        pg.draw.circle(surface, self.point_color, self.end, 3)

    def set_end(self, pos):
        self.end = pos
        self.moving = False
        self.distance = self.calculate_distance()

    def calculate_distance(self):
        p1 = self.start
        p2 = self.end
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def get_lerp_val(value):
    """ Get the the lerp value of based on max_value """
    max_value = 500
    if value > max_value:
        value = max_value
    percent = (value * 100) / max_value
    return percent / 100


def lerp(color_1, color_2, lerp_val):
    """
    Return a new color that is a linear interpolation of the two
    argument colors.  lerp_val must be between 0 and 1 (inclusive).
    """
    if not (0 <= lerp_val <= 1):
        raise ValueError("Lerp value must be in the range [0,1] inclusive.")
    new = [int(a * (1 - lerp_val) + b * lerp_val) for a, b in zip(color_1, color_2)]
    return pg.Color(*new)

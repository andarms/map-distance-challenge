import pygame as pg
import prepare

from state_engine import GameState
from line import Line


class MapViewer(GameState):
    """
    This state allows the user to view the map they selected from
    the menu.
    """
    def __init__(self):
        super(MapViewer, self).__init__()
        self.screen_rect = prepare.SCREEN.get_rect()

    def startup(self, persistent):
        self.persist = persistent
        self.map_name = self.persist["map name"]
        self.map = prepare.GFX[self.map_name.replace(" ", "-")]
        self.rect = self.map.get_rect(center=self.screen_rect.center)
        self.map_scale = prepare.SCALES[self.map_name]
        self.line = None

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True

        if event.type == pg.MOUSEBUTTONUP:
            if self.line and self.line.moving:
                self.line.set_end(event.pos)
            else:
                self.create_new_line(event.pos)

        if event.type == pg.MOUSEMOTION:
            if self.line and self.line.moving:
                self.line.end = event.pos

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill(pg.Color("gray2"))
        surface.blit(self.map, self.rect)
        if self.line:
            self.line.draw(surface)

    def create_new_line(self, pos):
        self.line = Line(pos)

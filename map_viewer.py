import pygame as pg
import prepare

from labels import Label
from line import Line
from state_engine import GameState


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
        self.distance = 0.0

        self.font = prepare.FONTS["Saniretro"]
        self.distance_label = None
        self.text_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True

        if event.type == pg.MOUSEBUTTONUP:
            if self.line and self.line.moving:
                self.set_anchor_point(event.pos)
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
            self.distance_label.draw(surface)

    def create_new_line(self, pos):
        self.line = Line(pos)
        self.distance = 0.0
        text = "{:.2f} miles".format(self.distance)
        self.distance_label = Label(self.font, 20, text,
                                    self.text_color, {"topleft": (0, 0)},
                                    self.bg_color)

    def set_anchor_point(self, pos):
        self.line.set_end(pos)
        self.distance = self.line.distance * self.map_scale
        text = "{:.2f} miles".format(self.distance)
        self.distance_label.set_text(text)

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

        self.lines = []
        self.is_path_end = False

        self.font = prepare.FONTS["Saniretro"]
        self.distance_label = None
        self.text_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)
        info = "Left click to add a point, Right click to end path"
        self.info_labe = Label(self.font, 20, info,
                               self.text_color,
                               {"bottomleft": self.screen_rect.bottomleft},
                               self.bg_color)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:  # left click
                if self.lines and self.lines[-1].moving:
                    self.set_anchor_point(event.pos)
                else:
                    if self.is_path_end:
                        self.create_new_path()
                    self.create_new_line(event.pos)

            if event.button == 3:  # right click
                self.end_path(event.pos)

        if event.type == pg.MOUSEMOTION:
            if self.lines and self.lines[-1].moving:
                self.lines[-1].end = event.pos

    def update(self, dt):
        if self.lines:
            for line in self.lines:
                line.update()

    def draw(self, surface):
        surface.fill(pg.Color("gray2"))
        surface.blit(self.map, self.rect)
        if self.lines:
            for line in self.lines:
                line.draw(surface)
            self.distance_label.draw(surface)
        self.info_labe.draw(surface)

    def create_new_line(self, pos):
        line = Line(pos)
        self.lines.append(line)
        text = "{:.2f} miles".format(0.0)
        self.distance_label = Label(self.font, 20, text,
                                    self.text_color, {"topleft": (0, 0)},
                                    self.bg_color)

    def set_anchor_point(self, pos):
        self.lines[-1].set_end(pos)
        self.distance_label.set_text(self.distance)
        line = Line(pos)
        self.lines.append(line)

    def create_new_path(self):
        self.lines = []

    def end_path(self, pos):
        self.lines[-1].set_end(pos)
        self.is_path_end = True

    @property
    def distance(self):
        distance = 0
        for line in self.lines:
            distance += line.distance * self.map_scale
        text = "{:.2f} miles".format(distance)
        return text

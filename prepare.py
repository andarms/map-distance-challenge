import os
import pygame as pg
import tools


SCREEN_SIZE = (650, 680)
ORIGINAL_CAPTION = "Map Viewer"

pg.init()
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

# Scale factors for the different maps
SCALES = {
    "North America": 600. / 68,
    "South America": 500. / 60,
    "Africa": 800. / 74,
    "Europe": 300. / 65,
    "Oceania": 600. / 45,
    "Asia": 800. / 76
}

GFX = tools.load_all_gfx(os.path.join("resources", "graphics"))
FONTS = tools.load_all_fonts(os.path.join("resources", "fonts"))

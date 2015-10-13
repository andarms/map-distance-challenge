import sys
import pygame as pg

from state_engine import Game
import prepare
import menu, map_viewer


states = {"MENU": menu.MenuScreen(),
          "MAPVIEWER": map_viewer.MapViewer()}

game = Game(prepare.SCREEN, states, "MENU")
game.run()
pg.quit()
sys.exit()

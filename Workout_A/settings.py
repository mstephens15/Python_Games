<<<<<<< HEAD
import pygame as pg

=======
>>>>>>> d79e971bfc59112cb07698c087686def975adb0a
# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# player settings
<<<<<<< HEAD
PLAYER_SPEED = 300
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_ROT_SPEED = 250
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

=======
PLAYER_IMG = 'manBlue_gun.png'
>>>>>>> d79e971bfc59112cb07698c087686def975adb0a

# wall settings
WALL_IMG = 'tileGreen_39.png'
from constants import *
from sprite import pg

WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768   # 16 * 48 or 32 * 24 or 64 * 12

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
FPS = 60
BGCOLOR = brown

# Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250    # degrees / second
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)   # the hitbox of the player

# Wall settings
WALL_IMG = 'tileGreen_39.png'

# Mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
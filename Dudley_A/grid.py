from constants import *
from sprite import pg
vec = pg.math.Vector2

WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768   # 16 * 48 or 32 * 24 or 64 * 12

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
FPS = 60
BGCOLOR = brown

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250    # degrees / second
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)   # the hitbox of the player
BARREL_OFFSET = vec(30, 10)

# Wall settings
WALL_IMG = 'tileGreen_39.png'

# Mob settings
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 30
MOB_IMG = 'zombie1_hold.png'
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)

# Gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFE = 1000
BULLET_RATE = 150    # how fast can we shoot the bullets
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10
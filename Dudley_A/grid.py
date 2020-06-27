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
MOB_SPEEDS = [150, 125, 100, 125, 150]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
AVOID_RADIUS = 50

# Gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFE = 1000
BULLET_RATE = 150    # how fast can we shoot the bullets
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10

# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png']
FLASH_DURATION = 40

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
MOB_LAYER = 2
BULLET_LAYER = 3
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'health_pack.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 15
BOB_SPEED = 0.35
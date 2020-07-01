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
DETECT_RADIUS = 400
SPLAT = 'splat red.png'

# Weapon settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500,
                     'bullet_life': 1000,
                     'bullet_rate': 150,
                     'bullet_damage': 10,
                     'kickback': 200,
                     'bullet_spread': 5,
                     'bullet_size': 'lg',
                     'bullet_count': 1}

WEAPONS['shotgun'] = {'bullet_speed': 300,
                     'bullet_life': 700,
                     'bullet_rate': 600,
                     'bullet_damage': 5,
                     'kickback': 300,
                     'bullet_spread': 18,
                     'bullet_size': 'sm',
                     'bullet_count': 12}
# BULLET_SPEED = 500
# BULLET_LIFE = 1000
# BULLET_RATE = 150    # how fast can we shoot the bullets
# KICKBACK = 200
# GUN_SPREAD = 5
# BULLET_DAMAGE = 10

# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png']
FLASH_DURATION = 40
DAMAGE_ALPHA = [i for i in range(0, 255, 25)]      # list comprehension

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
MOB_LAYER = 2
BULLET_LAYER = 3
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 15
BOB_SPEED = 0.35

# Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['sfx_weapon_singleshot2.wav'],
                 'shotgun': ['shotgun.wav']}
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav',
                  'gun_pickup': 'gun_pickup.wav'}
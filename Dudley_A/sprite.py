import pygame as pg
from grid import *
from tilemap import collide_hit_rect
vec = pg.math.Vector2
from random import uniform, choice, randint      # gives real number between bounds
import pytweening as tween

def collide_with_walls(sprite, group, dir):
    if dir == 'x':  # if the collision is horizontal, i.e. from x
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect) # recognize that the sprite collided
        if hits: # if it collided
            if hits[0].rect.centerx > sprite.hit_rect.centerx:  # if we were getting pushed right out of the blocks
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:  # if we were getting pushes left out of the blocks
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0  # make it stop
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':  # if the collision is vertical, i.e. from y
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:  # if we would be getting pushed underneath
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2   # it hit top of block, need to be at top minus our height
            if hits[0].rect.centery < sprite.hit_rect.centery:  # if we would be getting pushed above
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0  # make it stop
            sprite.hit_rect.centery = sprite.pos.y


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER      # make sure it is ._layer, that is a specific property
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)  # required
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()      # required
        self.rect.center = (x, y)              # fixes the bug of the guy moving around when placing new walls
        self.hit_rect = PLAYER_HIT_RECT        # spawning the hitbox of the player
        self.hit_rect.center = self.rect.center  # center of image is same as center of hitbox
        self.vel = vec(0, 0)                   # Velocity
        self.pos = vec(x, y)
        self.rot = 0                           # how far we've rotated
        self.last_shot = 0                     # havent shot yet when we spawn
        self.health = PLAYER_HEALTH

    def get_keys(self):
        self.rot_speed = 0          # setting rotation speed
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED    # spin counter-clockwise
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED   # spin clockwise
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)   # move forwards by coordinates (playerspeed, 0), but rotate based on self.rot
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)
        if keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now - self.last_shot > BULLET_RATE:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = self.pos + BARREL_OFFSET.rotate(-self.rot)        # this position of the bullet is offset from the center of the player
                Bullet(self.game, pos, dir)
                self.vel = vec(-KICKBACK, 0).rotate(-self.rot)          # gives a little kickback when shooting
                MuzzleFlash(self.game, pos)

    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360  # update our rotation by whatever the speed is, between (0,1)
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x      # checking for collisions from hitbox
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y      # checking for collisions from hitbox
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

    def add_health(self, amount):
        self.health += amount
        if self.health > PLAYER_HEALTH:
            self.health = PLAYER_HEALTH

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = MOB_LAYER
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)  # acceleration, so mob doesnt turn super fast
        self.rect.center = self.pos
        self.rot = 0
        self.health = MOB_HEALTH
        self.speed = choice(MOB_SPEEDS)             # choose random number from list of speeds

    def avoid_mobs(self):
        for mob in self.game.mobs:          # for every mob that isnt a specific mob we select
            if mob != self:
                dist = self.pos - mob.pos           # the distance between our first mob and any other mob
                if 0 < dist.length() < AVOID_RADIUS:
                    self.acc += dist.normalize()        # makes the vector a length of one


    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0)) # get the angle between player and mob
        self.image = pg.transform.rotate(self.game.mob_img, self.rot)    # update mob angle to go towards player
        self.rect = self.image.get_rect()     # makes him spin based on center of mob, not top lefthand of png
        self.rect.center = self.pos             # makes him position around where we originally put him on the map
        self.acc = vec(1, 0).rotate(-self.rot)  # move towards the player
        self.avoid_mobs()
        self.acc.scale_to_length(self.speed)             # takes the vector of 1 and gives it the speed
        self.acc += self.vel * -1                       # makes him hit a max speed he cant go higher than
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        if self.health <= 0:                    # if health falls to 0, the zombie is killed
            self.kill()

    def draw_health(self):
        if self.health > 60:
            col = green
        elif self.health > 30:
            col = yellow
        else:
            col = red
        width = int(self.rect.width * self.health / MOB_HEALTH)
        self.health_bar = pg.Rect(0, 0, width, 7)           # location on sprite image, not on screen
        if self.health < MOB_HEALTH:
            pg.draw.rect(self.image, col, self.health_bar)

class Bullet(pg.sprite.Sprite):
    def __init__(self, game, pos, dir):
        self._layer = BULLET_LAYER
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.bullet_img                # loaded in load_data in main
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.pos = vec(pos)                         # has a vector that is the same number, but is a copy so the player doesn't go where the bullet should
        self.rect.center = pos
        spread = uniform(-GUN_SPREAD, GUN_SPREAD)        # gives the bullet a random spread
        self.vel = dir.rotate(spread) * BULLET_SPEED     # randomly rotate the vector by the spread; BULLET_SPEED actually makes it go
        self.spawn_time = pg.time.get_ticks()            # lets us know when to delete the bullet

    def update(self):
        self.pos += self.vel * self.game.dt         # move at our velocity
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self, self.game.walls):    # if it hits any wall, delete it
            self.kill()
        if pg.time.get_ticks() - self.spawn_time > BULLET_LIFE:  # if the bullet has traveled too long, delete it
            self.kill()

# we arent drawing these, they will stay invisible; just has a rectangle
class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self._layer = WALL_LAYER
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Item(pg.sprite.Sprite):
    def __init__(self, game, pos, type):
        self._layer = ITEMS_LAYER
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.item_images[type]
        self.rect = self.image.get_rect()
        self.type = type
        self.rect.center = pos
        self.pos = pos
        self.tween = tween.easeInOutSine
        self.step = 0
        self.dir = 1        # for changing directions

    def update(self):
        # bobbing motion
        offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5)  # Need 0.5 because we are starting at middle of rectangle
        self.rect.centery = self.pos.y + offset * self.dir
        self.step += BOB_SPEED
        if self.step > BOB_RANGE:
            self.step = 0
            self.dir *= -1

class MuzzleFlash(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self._layer = EFFECTS_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        size = randint(20, 50)
        self.image = pg.transform.scale(choice(game.gun_flashes), (size, size))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = pos
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.spawn_time > FLASH_DURATION:
            self.kill()


    # took this out because we are now using Tiled obstacles, go back to this for reference
# class Wall(pg.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.groups = game.all_sprites, game.walls
#         pg.sprite.Sprite.__init__(self, self.groups)  # simply required for it to function
#         self.game = game
#         self.image = game.wall_img
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x * TILESIZE
#         self.rect.y = y * TILESIZE


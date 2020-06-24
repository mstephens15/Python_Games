import pygame as pg
from grid import *
from tilemap import collide_hit_rect
vec = pg.math.Vector2

def collide_with_walls(sprite, group, dir):
    if dir == 'x':  # if the collision is horizontal, i.e. from x
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect) # recognize that the sprite collided
        if hits: # if it collided
            if sprite.vel.x > 0:  # and if it was going right
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if sprite.vel.x < 0:  # and it was going left
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0  # make it stop
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':  # if the collision is vertical, i.e. from y
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.y > 0:  # and if it was going down
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2   # it hit top of block, need to be at top minus our height
            if sprite.vel.y < 0:  # and it was going up
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0  # make it stop
            sprite.hit_rect.centery = sprite.pos.y


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)  # required
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()      # required
        self.hit_rect = PLAYER_HIT_RECT        # spawning the hitbox of the player
        self.hit_rect.center = self.rect.center  # center of image is same as center of hitbox
        self.vel = vec(0, 0)                   # Velocity
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0                           # how far we've rotated

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

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)  # accelation, so mob doesnt turn super fast
        self.rect.center = self.pos
        self.rot = 0

    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0)) # get the angle between player and mob
        self.image = pg.transform.rotate(self.game.mob_img, self.rot)    # update mob angle to go towards player
        self.rect = self.image.get_rect()     # makes him spin based on center of mob, not top lefthand of png
        self.rect.center = self.pos             # makes him position around where we originally put him on the map
        self.acc = vec(MOB_SPEED, 0).rotate(-self.rot)  # move towards the player
        self.acc += self.vel * -1                       # makes him hit a max speed he cant go higher than
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)  # simply required for it to function
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
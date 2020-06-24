import pygame as pg
from grid import *
from tilemap import collide_hit_rect
vec = pg.math.Vector2

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


    def collide_with_walls(self, dir):
        if dir == 'x':  # if the collision is horizontal, i.e. from x
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect) # recognize that the sprite collided
            if hits: # if it collided
                if self.vel.x > 0:  # and if it was going right
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if self.vel.x < 0:  # and it was going left
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vel.x = 0  # make it stop
                self.hit_rect.centerx = self.pos.x
        if dir == 'y':  # if the collision is vertical, i.e. from y
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:  # and if it was going down
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2   # it hit top of block, need to be at top minus our height
                if self.vel.y < 0:  # and it was going up
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
                self.vel.y = 0  # make it stop
                self.hit_rect.centery = self.pos.y

    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360  # update our rotation by whatever the speed is, between (0,1)
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x      # checking for collisions from hitbox
        self.collide_with_walls('x')
        self.hit_rect.centery = self.pos.y      # checking for collisions from hitbox
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILESIZE
        self.rect.center = self.pos
        self.rot = 0

    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0)) # get the angle between player and mob
        self.image = pg.transform.rotate(self.game.mob_img, self.rot)    # update mob angle to go towards player
        self.rect = self.image.get_rect()     # makes him spin based on center of mob, not top lefthand of png
        self.rect.center = self.pos             # makes him position around where we originally put him on the map

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
import pygame as pg
from grid import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)  # required
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()      # required
        self.vel = vec(0, 0)                   # Velocity
        self.pos = vec(x, y) * TILESIZE

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071    # 1 / sqrt(2)

    def collide_with_walls(self, dir):
        if dir == 'x':  # if the collision is horizontal, i.e. from x
            hits = pg.sprite.spritecollide(self, self.game.walls, False) # recognize that the sprite collided
            if hits: # if it collided
                if self.vel.x > 0:  # and if it was going right
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:  # and it was going left
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0  # make it stop
                self.rect.x = self.pos.x
        if dir == 'y':  # if the collision is vertical, i.e. from y
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:  # and if it was going down
                    self.pos.y = hits[0].rect.top - self.rect.height # it hit top of block, need to be at top minus our height
                if self.vel.y < 0:  # and it was going upv
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0  # make it stop
                self.rect.y = self.pos.y

    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)  # simply required for it to function
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
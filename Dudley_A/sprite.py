import pygame as pg
from grid import *


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)  # required
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()      # required
        self.vx, self.vy = 0, 0                # Velocity
        self.x = x * TILESIZE                            # keeping track of where the sprite is
        self.y = y * TILESIZE                            # keeping track of where the sprite is

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071    # 1 / sqrt(2)
            self.vy *= 0.7071

    def collide_with_walls(self, dir):
        if dir == 'x':  # if the collision is horizontal, i.e. from x
            hits = pg.sprite.spritecollide(self, self.game.walls, False) # recognize that the sprite collided
            if hits: # if it collided
                if self.vx > 0:  # and if it was going right
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:  # and it was going left
                    self.x = hits[0].rect.right
                self.vx = 0  # make it stop
                self.rect.x = self.x
        if dir == 'y':  # if the collision is vertical, i.e. from y
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:  # and if it was going down
                    self.y = hits[0].rect.top - self.rect.height # it hit top of block, need to be at top minus our height
                if self.vy < 0:  # and it was going upv
                    self.y = hits[0].rect.bottom
                self.vy = 0  # make it stop
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt     # Finds location by pixel; i.e., 10 * 32 goes to 320 as top left hand corner
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
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
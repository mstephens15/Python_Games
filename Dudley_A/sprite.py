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
        self.x = x                             # keeping track of where the sprite is
        self.y = y                             # keeping track of where the sprite is

    # Lets us move in one direction; by default, it is zero. If i move dx = 1, then dy = 0 still, so it will only go
    # right or left

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE       # Finds location by pixel; i.e., 10 * 32 goes to 320 as top left hand corner
        self.rect.y = self.y * TILESIZE

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
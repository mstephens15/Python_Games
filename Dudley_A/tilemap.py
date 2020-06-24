from grid import *
import pygame as pg


def collide_hit_rect(one, two):                 # overriding spritecollision; checking for hitbox versus wall, not the typical sprite rectangle around it
    return one.hit_rect.colliderect(two.rect)
class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())  # takes away that last line in the text file that is present to say nothing follows (/n)

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height) # how far up, down, left, or right does it need to shift
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)  # gets new rectangle that shifts by a certain amount

    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # wont scroll too far -left-
        y = min(0, y)  # wont scroll too far -up-
        x = max((WIDTH - self.width), x) # wont scroll too far -right- ; WIDTH is 1048 pixels, self.width = 2048
        y = max((HEIGHT - self.height), y)  # wont scroll too far -down-

        self.camera = pg.Rect(x, y, self.width, self.height)
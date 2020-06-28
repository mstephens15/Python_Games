import pygame as pg
import pytmx
from settings import *

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

<<<<<<< HEAD
class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)       # making a quicker variable to load the map
        self.width = tm.width * tm.tilewidth                    # getting the width of any TiledMap loaded in
        self.height = tm.height * tm.tileheight                 # getting the height of any TiledMap loaded in
        self.tmxdata = tm                                       # all of that data
=======
class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
>>>>>>> d79e971bfc59112cb07698c087686def975adb0a

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Camera:
    def __init__(self, width, height):
<<<<<<< HEAD
        self.camera = pg.Rect(0, 0, width, height)      # use rectangle to track the camera
=======
        self.camera = pg.Rect(0, 0, width, height)
>>>>>>> d79e971bfc59112cb07698c087686def975adb0a
        self.width = width
        self.height = height

    def apply(self, entity):
<<<<<<< HEAD
        return entity.rect.move(self.camera.topleft)        # gives new rectangle shifted by .topleft amount
=======
        return entity.rect.move(self.camera.topleft)
>>>>>>> d79e971bfc59112cb07698c087686def975adb0a

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

<<<<<<< HEAD
    def update(self, target):                               # target is the sprite we are following
        x = -target.rect.centerx + int(WIDTH / 2)           # go in the opposite direction of the player; half the screen size to keep the player centered
        y = -target.rect.centery + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left; x takes the lower of 0 or x, so it can never be greater than 0
        y = min(0, y)  # top; has to be less than 0
        x = max(-(self.width - WIDTH), x)  # right; currently, -(2048-1024) or x
        y = max(-(self.height - HEIGHT), y)  # bottom; has to be greater than -(self.height - HEIGHT)
        self.camera = pg.Rect(x, y, self.width, self.height)    # adjusting what the rectangle is
=======
    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WIDTH), x)  # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
>>>>>>> d79e971bfc59112cb07698c087686def975adb0a

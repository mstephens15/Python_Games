from grid import *
import pygame as pg
import pytmx


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

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)       # pixel gives transparency
        self.width = tm.width * tm.tilewidth                    # width is how many tiles across the map is; tilewidth is how many pixels each tile is width wise
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm                                       # just to hold all of the data

    # makes surface, draws all tiles of map onto it
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid          # file image based on number in the tmx file, renaming the long command
        for layer in self.tmxdata.visible_layers:          # this looks at everything that is currently being displayed on the tmx (the little eye icon)
            if isinstance(layer, pytmx.TiledTileLayer):    # looked at tile layers, instead of object or image layers
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height) # how far up, down, left, or right does it need to shift
        self.width = width
        self.height = height

    def apply(self, entity):                         # apply offset to sprite
        return entity.rect.move(self.camera.topleft)  # gets new rectangle that shifts by a certain amount

    def apply_rect(self, rect):                      # apply offset to rectangle
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # wont scroll too far -left-
        y = min(0, y)  # wont scroll too far -up-
        x = max((WIDTH - self.width), x) # wont scroll too far -right- ; WIDTH is 1048 pixels, self.width = 2048
        y = max((HEIGHT - self.height), y)  # wont scroll too far -down-

        self.camera = pg.Rect(x, y, self.width, self.height)
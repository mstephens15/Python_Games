import sys
from sprites import *
from os import path
from tiledmap import *
from settings import *


class Game:
    def __init__(self):
        pg.init()                                               # required
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))      # required: from settings
        pg.display.set_caption(TITLE)                           # title
        self.clock = pg.time.Clock()                            # helps manage time
        pg.key.set_repeat(500, 100)                             # after half a second, if still holding down a key, it will start repeating
        self.load_data()                                        # calling load_data method from below

    def load_data(self):
        game_folder = path.dirname(__file__)                    # gets the file path of where this code is executed
        img_folder = path.join(game_folder, 'img')              # better way to join folders
        map_folder = path.join(game_folder, 'maps')             # better way to join folders
        self.map = TiledMap(path.join(map_folder, 'level1.tmx'))   # joins the TiledMap class
        self.map_img = self.map.make_map()                      # loads the full map
        self.map_rect = self.map_img.get_rect()                 # makes the rectangle of the map
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()    # keeps the transparent background that way
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.camera = Camera(self.map.width, self.map.height)
        for tile_object in self.map.tmxdata.objects:            # .objects gets all the object layers
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
        self.draw_debug = False

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0  # fix for Python 2.x
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))    # drawing the mpa
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))           # draw the sprites, apply the camera to the player
            if self.draw_debug:
                pg.draw.rect(self.screen, WHITE, self.camera.apply_rect(sprite.hit_rect), 1)  # shows hit rect of sprites
        if self.draw_debug:
            for wall in self.walls:                  # shows hit rect of walls
                pg.draw.rect(self.screen, WHITE, self.camera.apply_rect(wall.rect), 1)

        pg.display.flip()                               # think of whiteboard

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
import sys
from sprites import *
from os import path
from tiledmap import *
from settings import *


class Game:
    def __init__(self):
<<<<<<< HEAD
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
=======
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'level1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))
>>>>>>> d79e971bfc59112cb07698c087686def975adb0a

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self, 10, 10)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
<<<<<<< HEAD
        self.camera.update(self.player)
=======
>>>>>>> d79e971bfc59112cb07698c087686def975adb0a

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
<<<<<<< HEAD
        pg.display.flip()                               # think of whiteboard
=======
        pg.display.flip()
>>>>>>> d79e971bfc59112cb07698c087686def975adb0a

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

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
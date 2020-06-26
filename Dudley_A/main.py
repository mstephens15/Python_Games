from sprite import *
import sys
from os import path
from tilemap import *

# HUD Functions
def draw_player_health(surf, x, y, pct):
    if pct < 0:         # just in case it ever goes less than 0
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = green
    elif pct > 0.3:
        col = yellow
    else:
        col = red
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, white, outline_rect, 2)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.load_data()
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)   #

        # Title and Icon
        pg.display.set_caption("Dudley 1.0")
        icon = pg.image.load("sprites/pokemon.png")
        pg.display.set_icon(icon)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'level1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE,TILESIZE))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()  # creating the sprites group
        self.walls = pg.sprite.Group()        # creating the walls group
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        # for row, tiles in enumerate(self.map.data):  # Enumerate gets item and index number; this is to create the tiles
        #     for col, tile in enumerate(tiles):
        #         if tile == '1':
        #             Wall(self, col, row)
        #         if tile == "P":
        #             self.player = Player(self, col, row)
        #         if tile == "M":
        #             self.mob = Mob(self, col, row)
        self.player = Player(self, 5, 5)
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
        self.camera.update(self.player)  # can switch out self.player to have the camera track any sprite we want
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)     # zombie doesnt disappear, bullets do

      # player hits mob
        for hit in hits:
            hit.health -= BULLET_DAMAGE
            hit.vel = vec(0,0)

      # mob hits player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)       # knocked back by whatever mob that hit us' rotation is

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, lightgrey, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, lightgrey, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))  # chec king the fps at the top of the window
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))       # draws the map
        # self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):         # if it is a zombie, draw the health bar
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))  # applying the camera to the sprite
        # pg.draw.rect(self.screen, white, self.player.hit_rect, 2)  # draws little white box around hitbox
        # HUD functions
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

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

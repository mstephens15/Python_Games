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
        pg.mixer.pre_init(44100, -16, 4, 2048)
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.load_data()
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)   #

        # Title and Icon
        pg.display.set_caption("Dudley 1.0")
        icon = pg.image.load("sprites/pokemon.png")
        pg.display.set_icon(icon)

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.map_folder = path.join(game_folder, 'maps')
        snd_folder = path.join(game_folder, 'snd')
        music_folder = path.join(game_folder, 'music')
        self.title_font = path.join(img_folder, 'ZOMBIE.TTF')                 # title font, pause menu
        self.hud_font = path.join(img_folder, 'Impacted2.0.ttf')
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()        # dim screen when paused, pt1
        self.dim_screen.fill((0, 0, 0, 180))                                        # dim screen when paused, pt2
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()      # player img
        self.bullet_images = {}
        self.bullet_images['lg'] = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()      # bullet img
        self.bullet_images['sm'] = pg.transform.scale(self.bullet_images['lg'], (10,10))
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()            # zombie img
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()          # wall img
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE,TILESIZE))                  # converts the wall img size to what we want because that would be hard to do in Tiled app
        self.splat = pg.image.load(path.join(img_folder, SPLAT)).convert_alpha()
        self.splat = pg.transform.scale(self.splat, (64, 64))                                   # changing splat size from 128x128 to 64x64
        self.gun_flashes = []       # list to hold the 3 muzzle flash effects
        for img in MUZZLE_FLASHES:
            self.gun_flashes.append(pg.image.load(path.join(img_folder, img)).convert_alpha())    # puts all the muzzle flash pngs in that list that we can now mess with
        self.item_images = {}       # dictionary to hold all of the item images keys and values
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()    # different from the one above, because we wont be selecting these randomly

                # Lighting effect
        self.fog = pg.Surface((WIDTH, HEIGHT))
        self.fog.fill(NIGHT_COLOR)
        self.light_mask = pg.image.load(path.join(img_folder, LIGHT_MASK)).convert_alpha()
        self.light_mask = pg.transform.scale(self.light_mask, LIGHT_RADIUS)
        self.light_rect = self.light_mask.get_rect()

                # Sound loading

        pg.mixer.music.load(path.join(music_folder, BG_MUSIC))   # loads the music we want

        self.effects_sounds = {}        # effects sounds, see ('player picks up item') in main.py
        for type in EFFECTS_SOUNDS:
            self.effects_sounds[type] = pg.mixer.Sound(path.join(snd_folder, EFFECTS_SOUNDS[type]))
        self.weapon_sounds = {}
        for weapon in WEAPON_SOUNDS:
            self.weapon_sounds[weapon] = []
            for snd in WEAPON_SOUNDS[weapon]:
                s = pg.mixer.Sound(path.join(snd_folder, snd))
                s.set_volume(0.3)
                self.weapon_sounds[weapon].append(s)
        self.zombie_moan_sounds = []    # zombie sounds, see (sprite.mob)
        for snd in ZOMBIE_MOAN_SOUNDS:
            s = pg.mixer.Sound(path.join(snd_folder,snd))
            s.set_volume(0.1)                                  # between 0 and 1, 1 is what it currently is
            self.zombie_moan_sounds.append(s)
        self.player_hit_sounds = []     # player sounds
        for snd in PLAYER_HIT_SOUNDS:
            self.player_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd)))
        self.zombie_hit_sounds = []     # zombie dying sounds
        for snd in ZOMBIE_HIT_SOUNDS:
            self.zombie_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd)))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.LayeredUpdates()  # creating the sprites group
        self.walls = pg.sprite.Group()        # creating the walls group
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.map = TiledMap(path.join(self.map_folder, 'level1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        # for row, tiles in enumerate(self.map.data):  # Enumerate gets item and index number; this is to create the tiles
        #     for col, tile in enumerate(tiles):
        #         if tile == '1':
        #             Wall( self, col, row)
        #         if tile == "P":
        #             self.player = Player(self, col, row)
        #         if tile == "M":
        #             self.mob = Mob(self, col, row)
        for tile_object in self.map.tmxdata.objects:            # holds all objects from all objects layers
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)          # centers the spawn points around the boxes in Tiled
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)        # spawn player
            if tile_object.name == 'zombie':
                Mob(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)   # spawn obstacle
            if tile_object.name in ['health', 'shotgun']:       # looking for any item pickups
                Item(self, obj_center, tile_object.name)
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False                                 # whether hit boxes are drawn or not
        self.paused = False                                     # whether game is paused or not
        self.night = False
        self.effects_sounds['level_start'].play()

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        pg.mixer.music.play(loops=-1)       # -1 makes it repeat
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            if not self.paused:
                self.update()               # this is what updates everything, making things go in motion; turning off freezes everyhing
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)  # can switch out self.player to have the camera track any sprite we want

      # game over condition


        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)     # zombie doesnt disappear, bullets do

      # player hits mob
        for mob in hits:
            # hit.health -= WEAPONS[self.player.weapon]['bullet_damage'] * len(hits[hit])     # gets dictionary of how many bullets hit it, hense len
            for bullet in hits[mob]:
                mob.health -= bullet.damage
            mob.vel = vec(0,0)

      # player picks up item
        hits = pg.sprite.spritecollide(self.player, self.items, False)
        for hit in hits:
            if hit.type == 'health' and self.player.health < PLAYER_HEALTH:
                hit.kill()
                self.effects_sounds['health_up'].play()     # play sound effect of picking up health
                self.player.add_health(HEALTH_PACK_AMOUNT)
            if hit.type == 'shotgun':
                hit.kill()
                self.effects_sounds['gun_pickup'].play()
                self.player.weapon = 'shotgun'

      # mob hits player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            if random() < 0.7:
                choice(self.player_hit_sounds).play()       # play random noise of guy saying "ah"
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.hit()
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)       # knocked back by whatever mob that hit us' rotation is

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, lightgrey, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, lightgrey, (0, y), (WIDTH, y))

    def render_fog(self):
        # draw the light mask (gradient) onto fog image
        self.fog.fill(NIGHT_COLOR)
        self.light_rect.center = self.camera.apply(self.player).center
        self.fog.blit(self.light_mask, self.light_rect)
        self.screen.blit(self.fog, (0, 0), special_flags=pg.BLEND_MULT)

    def draw(self):         # drawing everything on screen
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))  # checking the fps at the top of the window
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))       # draws the map
        # self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):         # if it is a zombie, draw the health bar
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))  # applying the camera to the sprite
            if self.draw_debug:
                pg.draw.rect(self.screen, white, self.camera.apply_rect(sprite.hit_rect), 1)
        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, white, self.camera.apply_rect(wall.rect), 1)

        # pg.draw.rect(self.screen, white, self.player.hit_rect, 2)  # draws little white box around hitbox

        if self.night:
            self.render_fog()

        # HUD functions
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        self.draw_text('Zombies: {}'.format(len(self.mobs)), self.hud_font,
                       30, white, WIDTH - 10, 10, align="ne")
        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))                                                        # put it at 0,0 to cover full screen
            self.draw_text("Paused", self.title_font, 105, red, WIDTH/2, HEIGHT/2, align="center")          # drawing pause screen
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:                         # toggle debug mode
                    self.draw_debug = not self.draw_debug
                if event.key == pg.K_p:                         # toggle pause
                    self.paused = not self.paused
                if event.key == pg.K_n:                         # toggle night mode
                    self.night = not self.night

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        self.screen.fill(black)
        self.draw_text("GAME OVER", self.title_font, 100,
                       red, WIDTH / 2, HEIGHT / 2, align="center")
        self.draw_text("Press a key to start", self.title_font, 75,
                       white, WIDTH / 2, HEIGHT * 3/4, align="center")
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        pg.event.wait()         # clears the queue of keys, so you dont have the key pressed when dying so it starts right away
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()

import pygame
import random
import time
from pygame import mixer  # For background music and sounds

# Done every time
pygame.init()

# Screen
screen = pygame.display.set_mode((800,600))

# Constants
bright_green = (0, 255, 0)
green = (0, 155, 0)
black = (0, 0, 0)

smallText = pygame.font.Font("freesansbold.ttf",16)

left = pygame.K_LEFT
right = pygame.K_RIGHT
up = pygame.K_UP
down = pygame.K_DOWN
clock = pygame.time.Clock()

# Background Music

# Sprite

class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.standing = True
        self.walkCount = 0

    def draw(self,screen):
        if (self.walkCount + 1) >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.up or self.down:
                screen.blit(character, (self.x, self.y))
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                screen.blit(walkLeft[0], (self.x, self.y))
            elif self.up or self.down:
                screen.blit(character, (self.x, self.y))
            else:
                screen.blit(character, (self.x, self.y))

man = player(50, 425, 64, 64)

    # Animations
walkRight = [pygame.image.load('GameAnimations/R1.png'), pygame.image.load('GameAnimations/R2.png'), pygame.image.load('GameAnimations/R3.png'),
             pygame.image.load('GameAnimations/R4.png'), pygame.image.load('GameAnimations/R5.png'), pygame.image.load('GameAnimations/R6.png'),
             pygame.image.load('GameAnimations/R7.png'), pygame.image.load('GameAnimations/R8.png'), pygame.image.load('GameAnimations/R9.png')]
walkLeft = [pygame.image.load('GameAnimations/L1.png'), pygame.image.load('GameAnimations/L2.png'), pygame.image.load('GameAnimations/L3.png'),
            pygame.image.load('GameAnimations/L4.png'), pygame.image.load('GameAnimations/L5.png'), pygame.image.load('GameAnimations/L6.png'),
            pygame.image.load('GameAnimations/L7.png'), pygame.image.load('GameAnimations/L8.png'), pygame.image.load('GameAnimations/L9.png')]
character = pygame.image.load('GameAnimations/standing.png')
# Level 1
level1Img = pygame.image.load("cotton-pad.png")
level1X = 368
level1Y = 450

# Level 2
level2Img = pygame.image.load("cotton-pad.png")
level2X = 368
level2Y = 336

# Trees on left side
treeImg = []
tree_leftX = []
tree_leftY = []
num_trees = 50

# Trees on right side
tree_rightX = []
tree_rightY = []
num_trees = 50

for i in range(num_trees):
    treeImg.append(pygame.image.load("tree.png"))
    tree_leftX.append(random.randint(0,300))
    tree_leftY.append(random.randint(0,550))
    tree_rightX.append(random.randint(450,750))
    tree_rightY.append(random.randint(0,550))

## Functions
def redrawScreen():
    man.draw(screen)
    pygame.display.update()

def draw_level(x, y):
    screen.blit(level1Img, (x, y))

def draw_level2(x, y):
    screen.blit(level2Img, (x, y))

def draw_trees(x, y, i):
    screen.blit(treeImg[i], (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def draw_button(msg, x, y, w, h, inactive, active):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, active, (x,y,w,h))
    else:
        pygame.draw.rect(screen, inactive, (x,y,w,h))

        # Button Text
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def replace(x, y):
    transparent = (0,0,0,0)
    replaceImg = pygame.image.load("tree.png")
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        level1Img.fill(transparent)
        screen.blit(replaceImg, (x, y))

# Window Loop
running = True
while running:
    clock.tick(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((100,150,180))

    draw_level(level1X, level1Y)
    draw_level2(level2X, level2Y)
    draw_button("Complete", 355, 550, 90, 30, green, bright_green)

    for i in range(num_trees):
        draw_trees(tree_leftX[i], tree_leftY[i], i)
        draw_trees(tree_rightX[i], tree_rightY[i], i)

    # Lines between levels
    pygame.draw.line(screen, black, (level1X + 32,level1Y), (level2X + 32,level2Y + 64), 5)

    # for event in pygame.event.get():
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         print("works")
    #         level1Img.fill((0,0,0,0))
    #         replace(level1X, level1Y)
    # replace(level1X, level1Y)


    # Movement
    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.up = False
        man.down = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 800-man.width-man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.up = False
        down = False
        man.standing = False
    elif keys[pygame.K_UP] and man.y > man.vel:
        man.y -= man.vel
        man.left = False
        man.right = False
        man.up = True
        man.down = False
        man.standing = False
    elif keys[pygame.K_DOWN] and man.y < 600 - man.height - man.vel:
        man.y += man.vel
        man.left = False
        man.right = False
        man.up = False
        man.down = True
        man.standing = False
    else:
        man.standing = True
        man.walkcount = 0

    redrawScreen()
pygame.quit()
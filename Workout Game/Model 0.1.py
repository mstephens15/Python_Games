import pygame
import random
from pygame import mixer  # For background music and sounds

# Done every time
pygame.init()

# Screen
screen = pygame.display.set_mode((800,600))

# Colors
bright_green = (0, 255, 0)
green = (0, 155, 0)
black = (0, 0, 0)

# Constants
smallText = pygame.font.Font("freesansbold.ttf",16)

left = pygame.K_LEFT
right = pygame.K_RIGHT
up = pygame.K_UP
down = pygame.K_DOWN

# Background

# Background Music

# Title and Icon
pygame.display.set_caption("Dudley Model 0.1")
icon = pygame.image.load("cotton-pad.png")
pygame.display.set_icon(icon)

# Sprite
guy = pygame.image.load("weak.png")
guyX = 50
guyY = 425
guyX_change = 0
guyY_change = 0

    # Sprite Movement
width = 60
height = 60
vel = 5

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
def draw_level(x, y):
    screen.blit(level1Img, (x, y))

def draw_level2(x, y):
    screen.blit(level2Img, (x, y))

def draw_trees(x, y, i):
    screen.blit(treeImg[i], (x, y))

def draw_sprite(x, y):
    screen.blit(guy, (x, y))

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
    screen.fill((100,150,180))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == left and guyX > vel:
                guyX_change = -5
            if event.key == right and guyX < 500-width-vel:
                guyX_change = 5
            if event.key == up and guyY > vel:
                guyY_change = -5
            if event.key == down and guyY < 500 - height - vel:
                guyY_change = 5
        if event.type == pygame.KEYUP:
            if event.key == left or event.key == right or event.key == up or event.key == down:
                playerX_change = 0

    guyX += guyX_change
    guyY += guyY_change

    if guyX <= 0:
        guyX = 0
    elif guyX >= 736:
        guyX = 736

    if guyY <= 0:
        guyY = 0
    elif guyY >= 550:
        guyY = 550

    draw_sprite(guyX, guyY)

    pygame.display.update()
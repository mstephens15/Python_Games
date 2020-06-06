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

# Background

# Background Music

# Title and Icon
pygame.display.set_caption("Dudley Model 0.1")
icon = pygame.image.load("cotton-pad.png")
pygame.display.set_icon(icon)

# Mission Complete Button


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

def draw_trees(x, y, i):
    screen.blit(treeImg[i], (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def draw_button(msg, x, y, w, h, inactive, active):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    replaceImg = pygame.image.load("tree.png")
    def replace(x, y):
        screen.blit(replaceImg, (x, y))

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, active, (x,y,w,h))
        if click[0] == 1:
            replace(level1X, level1Y)
            pygame.display.update()
    else:
        pygame.draw.rect(screen, inactive, (x,y,w,h))

        # Button Text
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

# Window Loop
running = True
while running:

    screen.fill((100,150,180))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_level(level1X, level1Y)
    draw_level(level2X, level2Y)
    draw_button("Complete", 355, 550, 90, 30, green, bright_green)

    for i in range(num_trees):
        draw_trees(tree_leftX[i], tree_leftY[i], i)
        draw_trees(tree_rightX[i], tree_rightY[i], i)

    # Lines between levels
    pygame.draw.line(screen, black, (level1X + 32,level1Y), (level2X + 32,level2Y + 64), 5)

    pygame.display.update()
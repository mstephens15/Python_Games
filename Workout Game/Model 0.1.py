import pygame
import random
from pygame import mixer  # For background music and sounds

# Done every time
pygame.init()

# Screen
screen = pygame.display.set_mode((800,600))

# Background

# Background Music

# Title and Icon
pygame.display.set_caption("Dudley Model 0.1")
icon = pygame.image.load("cotton-pad.png")
pygame.display.set_icon(icon)

# Level 1
level1Img = pygame.image.load("cotton-pad.png")
level1X = 368
level1Y = 500

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

# Window Loop
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((100,150,180))

        draw_level(level1X, level1Y)
        draw_level(level2X, level2Y)

        for i in range(num_trees):
            draw_trees(tree_leftX[i], tree_leftY[i], i)
            draw_trees(tree_rightX[i], tree_rightY[i], i)

        black = 0, 0, 0
        pygame.draw.line(screen, black, (level1X + 32,level1Y), (level2X + 32,level2Y + 64), 5)
        pygame.display.update()
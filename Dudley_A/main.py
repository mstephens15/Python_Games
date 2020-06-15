import pygame
from grid import *

# Initialization
pygame.init()
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Dudley 1.0")
icon = pygame.image.load("sprites/pokemon.png")
pygame.display.set_icon(icon)

# Screen
screen = pygame.display.set_mode((750,500))

# Main Loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display fill and update

    screen.fill((100,150,180))

    # RENDER GAME GRID
    for row in range(Mapheight):
        for column in range(Mapwidth):
            displaysurf.blit(Textures[Grid[row][column]], (column*Tilesize, row*Tilesize))

    pygame.display.update()

pygame.quit()
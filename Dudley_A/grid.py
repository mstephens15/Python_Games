import pygame
from constants import *

# Tiles
Dirt = 0
Grass = 1
Water = 2
Pad = 3

# Dictionary of pictures
Textures = {
    Dirt: pygame.image.load('./textures/dirt.png'),
    Grass: pygame.image.load('./textures/grass.png'),
    Water: pygame.image.load('./textures/water.png'),
    Pad: pygame.image.load('./textures/square.png')
}

Grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,3,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

Tilesize = 50
Mapwidth = 15
Mapheight = 10

displaysurf = pygame.display.set_mode((Mapwidth*Tilesize, Mapheight*Tilesize))
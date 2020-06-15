import pygame
# Tiles

Dirt = 0
Grass = 1
Water = 2

# Dictionary of pictures

Textures = {
    Dirt: pygame.image.load('./Sprites/dirt.png'),
    Grass: pygame.image.load('./Sprites/grass.png'),
    Water: pygame.image.load('./Sprites/water.png'),
}

GRID = [
    [Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass],
    [Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt],
    [Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass],
    [Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt],
    [Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass],
    [Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt],
    [Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water],
    [Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt],
    [Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water],
    [Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass],
    [Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water],
    [Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt],
]

Tilesize = 40
Mapwidth = 20
Mapheight = 11

displaysurf = pygame.display.set_mode((Mapwidth*Tilesize, Mapheight*Tilesize))
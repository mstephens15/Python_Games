import pygame

# Tiles
Dirt = 0
Grass = 1
Water = 2

# Dictionary of pictures
Textures = {
    Dirt: pygame.image.load('./sprites/dirt.png'),
    Grass: pygame.image.load('./sprites/grass.png'),
    Water: pygame.image.load('./sprites/water.png'),
}

Grid = [
    [Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass],
    [Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt],
    [Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass],
    [Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt],
    [Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass],
    [Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt],
    [Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water],
    [Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt, Dirt],
    [Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water, Water],
    [Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass,Grass]
]

Tilesize = 50
Mapwidth = 15
Mapheight = 10

displaysurf = pygame.display.set_mode((Mapwidth*Tilesize, Mapheight*Tilesize))
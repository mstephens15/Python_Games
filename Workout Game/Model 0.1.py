import pygame
from pygame import mixer  # For background music and sounds

# Done every time
pygame.init()

# Screen
screen = pygame.display.set_mode((800,600))

# Background

# Background Music

# Title and Icon

# Window Loop
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((100,150,180))


        pygame.display.update()
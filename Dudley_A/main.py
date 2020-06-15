import pygame

# Initialization
pygame.init()
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Dudley 1.0")
icon = pygame.image.load("sprites/pokemon.png")
pygame.display.set_icon(icon)

# Main Loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display fill and update

    screen.fill((100,150,180))
    pygame.display.update()

pygame.quit()
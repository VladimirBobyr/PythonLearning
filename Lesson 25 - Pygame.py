
# Install package from commandline:
# python -m pip install --user pygame

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

while True:
    pygame.display.flip()
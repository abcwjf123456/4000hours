import pygame, sys
from pygame.locals import *

pygame.init()
fps = 30
fpsclock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 0)
pygame.display.set_caption("动画")
RED = (255, 0, 0)
DISPLAYSURF.fill(RED)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsclock.tick(fps)

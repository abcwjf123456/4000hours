# 绘制函数
import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURY = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('绘制函数')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAYSURY.fill(WHITE)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

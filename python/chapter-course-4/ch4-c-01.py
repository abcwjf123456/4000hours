import pygame, sys
from pygame.locals import *

pygame.init()
fps = 60
size = width, height = 600, 400
speed = [1, 1]
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((size))
pygame.display.set_caption("pygame")
ball = pygame.image.load("搜狗截图.png")
ballrect = ball.get_rect()  # 将小球成为一个矩形
fclock = pygame.time.Clock()  # 设置最大帧速率

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:# 待完善
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] - 1
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] + 1

    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(BLACK)  # 一定需要这不然会出现连续图片
    screen.blit(ball, ballrect)  # blit(src,dest)函数将一个图像上，即将src绘制到dest位置上通过RECT对象引导对壁球的绘制
    pygame.display.update()
    fclock.tick(fps)  # 刷新速率

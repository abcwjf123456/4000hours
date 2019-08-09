import pygame
import sys
import settings



def run_game():
    pygame.init()
    ai_settings=settings.Settings()
    screen=pygame.display.set_mod()
    while True:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()


run_game()

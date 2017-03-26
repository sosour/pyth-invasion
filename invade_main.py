import pygame
import sys

from settings import Settings
from sloth import Sloth


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Invasion")

    sloth = Sloth(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        sloth.blitme()

        pygame.display.flip()

run_game()

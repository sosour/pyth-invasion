import pygame
import sys

from settings import Settings
from sloth import Sloth
import gfunctions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Invasion")

    sloth = Sloth(screen)

    while True:
        gf.check_events()
        
        gf.update_screen(ai_settings, screen, sloth)


run_game()

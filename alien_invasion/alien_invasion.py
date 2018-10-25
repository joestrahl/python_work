import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make an alien
    alien = Alien(ai_settings, screen)
    
    # Make a ship
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    #Create a new fleet of aliens
    gf.create_fleet(ai_settings, screen,ship, aliens)

    #Start the main loop for the game.
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        #make the most recently drawn screen visible.
        pygame.display.flip()
        
run_game()

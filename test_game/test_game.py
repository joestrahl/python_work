import sys

import pygame



def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Booty Pic")
    
    bg_color = (0, 0, 230)
    
    image = pygame.image.load('images/booty.png')
    rect = image.get_rect()
    screen_rect = screen.get_rect()
    
    rect.centerx = screen_rect.centerx
    rect.centery = screen_rect.centery
    
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.fill(bg_color)
        screen.blit(image, rect)
        

        pygame.display.flip()
        
        
             
run_game()

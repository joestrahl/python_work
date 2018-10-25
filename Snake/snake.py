import pygame
import random
import os
import sys



def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Snake')
    screen.fill((230, 230, 230))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        
        pygame.display.flip()
    
run_game()

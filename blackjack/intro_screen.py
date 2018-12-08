import pygame
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 100)

class Intro():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/title.png')
        self.image = pygame.transform.scale(self.image, (1200, 800))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
       
        
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        

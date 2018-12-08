
import pygame
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 25)

class Player_Select():
    
    def __init__(self, screen):
        self.screen = screen
        
        self.image1 = pygame.image.load('images/1_unpressed.png')
        self.image1 = pygame.transform.scale(self.image1, (100, 100))
        self.image2 = pygame.image.load('images/2_unpressed.png')
        self.image2 = pygame.transform.scale(self.image2, (100, 100))
        self.image3 = pygame.image.load('images/3_unpressed.png')
        self.image3 = pygame.transform.scale(self.image3, (100, 100))
        self.message = myfont.render('Select the number of players by typing 1, 2, or 3', False, (0, 0, 0,))
        
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect3 = self.image3.get_rect()
        self.message_rect = self.message.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect1.centery = self.screen_rect.centery
        self.rect2.centery = self.screen_rect.centery
        self.rect3.centery = self.screen_rect.centery
        self.message_rect.centery = 2*self.screen_rect.centery/3
        
        self.rect1.centerx = self.screen_rect.right/3
        self.rect2.centerx = self.screen_rect.centerx
        self.rect3.centerx = 2*self.screen_rect.right/3
        self.message_rect.centerx = self.screen_rect.centerx
    
    def blitme(self):
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.image2, self.rect2)
        self.screen.blit(self.image3, self.rect3)
        self.screen.blit(self.message, self.message_rect)

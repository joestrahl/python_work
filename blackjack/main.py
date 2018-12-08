import pygame as pg
pg.font.init()
myfont = pg.font.SysFont('Arial', 100)
from bjfunctions import *

class cardplay():
    def __init__(self, screen):
        self.screen = screen
        
        self.screen_rect = screen.get_rect()

        self.image = pg.image.load('images/cardfront.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
            
    
    def suit_display(self, card):
        
        self.suit = card['suit']
        self.card_rect = card.rect
        
        if suit == 'diamonds':
            self.suit_image = pg.image.load('images/diamond')
            self.suit_rect = self.suit_image.get_rect()
            self.suit_rect.right = card.rect.right - 10
            self.suit_rect.top = card.rect.top + 10
            
        if suit == 'clubs':
            self.suit_image = pg.image.load('images/club')
            self.suit_rect = self.suit_image.get_rect()
            self.suit_rect.right = card.rect.right - 10
            self.suit_rect.top = card.rect.top + 10
            
        if suit == 'spades':
            self.suit_image = pg.image.load('images/spade')
            self.suit_rect = self.suit_image.get_rect()
            self.suit_rect.right = card.rect.right - 10
            self.suit_rect.top = card.rect.top + 10
            
        if suit == 'hearts':
            self.suit_image = pg.image.load('images/heart')
            self.suit_rect = self.suit_image.get_rect()
            self.suit_rect.right = card.rect.right - 10
            self.suit_rect.top = card.rect.top + 10
            
        
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.suit_image, self.suit_rect)
        

import pygame as pg
pg.font.init()
myfont = pg.font.SysFont('Arial', 100)
myfont2 = pg.font.SysFont('Arial', 60)
import bjfunctions as bjf

class Card_Display():
    def __init__(self, screen, card, x, y):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pg.image.load('images/cardfront.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.left + x
        self.rect.centery = self.screen_rect.top + y
        
        self.suit = card['suit']
        
        x_shift = 45
        y_shift = 30
        
        if self.suit == 'diamonds':
            self.suit_image = pg.image.load('images/diamond.png')
            self.suit_rect = self.suit_image.get_rect()
            self.suit_rect.right = self.rect.right - x_shift
            self.suit_rect.top = self.rect.top + y_shift
            
        elif self.suit == 'clubs':
            self.suit_image = pg.image.load('images/club.png')
            self.suit_rect = self.suit_image.get_rect()
            self.suit_rect.right = self.rect.right - x_shift
            self.suit_rect.top = self.rect.top + y_shift
            
        elif self.suit == 'spades':
            self.suit_image = pg.image.load('images/spade.png')
            self.suit_rect = self.suit_image.get_rect()
            self.suit_rect.right = self.rect.right - x_shift
            self.suit_rect.top = self.rect.top + y_shift
            
        elif self.suit == 'hearts':
            self.suit_image = pg.image.load('images/heart.png')
            self.suit_rect = self.suit_image.get_rect()
            self.suit_rect.right = self.rect.right - x_shift
            self.suit_rect.top = self.rect.top + y_shift
            
        self.number = card['type']
        
        self.num_display = myfont.render(self.number, False, (0, 0, 0))
        self.num_rect = self.num_display.get_rect()
        self.num_rect.centerx = self.rect.centerx
        self.num_rect.centery = self.rect.centery
            
        
    
    def blitme_card(self):
        self.screen.blit(self.image, self.rect)

    def blitme_details(self):
        self.screen.blit(self.suit_image, self.suit_rect)
        self.screen.blit(self.num_display, self.num_rect)
        
class Bust_Display():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bust_display = myfont.render('BUST', False, (0, 0, 0))
        self.bust_rect = self.bust_display.get_rect()
        self.bust_rect.centerx = self.screen_rect.centerx
        self.bust_rect.centery = self.screen_rect.centery
        
    def blitme(self):
        self.screen.blit(self.bust_display, self.bust_rect)
        
class Win():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bust_display = myfont.render('You Win!', False, (0, 0, 0))
        self.bust_rect = self.bust_display.get_rect()
        self.bust_rect.centerx = self.screen_rect.centerx
        self.bust_rect.centery = self.screen_rect.centery
        
    def blitme(self):
        self.screen.blit(self.bust_display, self.bust_rect)
        
class Push():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bust_display = myfont.render('Push!', False, (0, 0, 0))
        self.bust_rect = self.bust_display.get_rect()
        self.bust_rect.centerx = self.screen_rect.centerx
        self.bust_rect.centery = self.screen_rect.centery
        
    def blitme(self):
        self.screen.blit(self.bust_display, self.bust_rect)
        
class Lose():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bust_display = myfont.render('You Lose!', False, (0, 0, 0))
        self.bust_rect = self.bust_display.get_rect()
        self.bust_rect.centerx = self.screen_rect.centerx
        self.bust_rect.centery = self.screen_rect.centery
        
    def blitme(self):
        self.screen.blit(self.bust_display, self.bust_rect)
        
class Chip_Display():
    def __init__(self, screen, player):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.display = myfont2.render('Chip Count: ' + str(player.chips), False, (0, 0, 0))
        self.rect = self.display.get_rect()
        self.rect.left = self.screen_rect.left + 10
        self.rect.bottom = self.screen_rect.bottom - 10
        
    def blitme(self):
        self.screen.blit(self.display, self.rect)

class Score_Display():
    def __init__(self, screen, player):
        score = player.player_score()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.display = myfont2.render(str(score), False, (0, 0, 0))
        self.rect = self.display.get_rect()
        self.rect.centery = self.screen_rect.top + 600
        self.rect.left = self.screen_rect.left + 10
        
    def blitme(self):
        self.screen.blit(self.display, self.rect)
        
class Dealer_Score_Display():
    def __init__(self, screen, player):
        score = player.player_score()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.display = myfont2.render(str(score), False, (0, 0, 0))
        self.rect = self.display.get_rect()
        self.rect.left = self.screen_rect.left + 10
        self.rect.centery = self.screen_rect.top + 200
        
    def blitme(self):
        self.screen.blit(self.display, self.rect)

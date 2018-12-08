import pygame
import random
import os
import bjsettings as bjs
from time import sleep
import main_card_functions as mcf
pygame.font.init()
myfont2 = pygame.font.SysFont('Arial', 60)

class Deck():
    # Establish the deck
    def __init__(self, number_of_decks=1):
        self.number_decks = number_of_decks
        card_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        suits = ['diamonds', 'clubs', 'spades', 'hearts']

        self.deck = []
        
        for suit in suits:
            for card_number in card_numbers:
                self.deck.append(suit + card_number)
                
    def shuffle(self):
        self.number_decks = number_of_decks
        card_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        suits = ['diamonds', 'clubs', 'spades', 'hearts']

        self.deck = []
        
        for suit in suits:
            for card_number in card_numbers:
                self.deck.append(suit + card_number)
                
class Dealer():
    # Establish the dealer cards
    def __init__(self, Deck):
        self.card1 = random.choice(Deck.deck)
        Deck.deck.remove(self.card1)
        self.card2 = random.choice(Deck.deck)
        Deck.deck.remove(self.card2)
        
        self.score = 0
        
        
        
        self.cards = [self.card1, self.card2]
        
        self.dcard1 = {'suit': None, 'type': '0'}
        self.dcard2 = {'suit': None, 'type': '0'}
        self.dcard3 = {'suit': None, 'type': '0'}
        self.dcard4 = {'suit': None, 'type': '0'}
        self.dcard5 = {'suit': None, 'type': '0'}
        self.dcard6 = {'suit': None, 'type': '0'}
        
        # detailed cards
        self.dcards = []
        
        self.card3 = False
        self.card4 = False
        self.card5 = False
        self.card6 = False
        
    # Draw another card for the dealer    
    def hit(self, Deck):
        self.score = 0
        for cardnumber in self.cards:
            if cardnumber[-1] == '2':
                self.score += 2
            elif cardnumber[-1] == '3':
                self.score += 3
            elif cardnumber[-1] == '4':
                self.score += 4
            elif cardnumber[-1] == '5':
                self.score += 5
            elif cardnumber[-1] == '6':
                self.score += 6
            elif cardnumber[-1] == '7':
                self.score += 7
            elif cardnumber[-1] == '8':
                self.score += 8
            elif cardnumber[-1] == '9':
                self.score += 9
            elif cardnumber[-1] == 'T':
                self.score += 10
            elif cardnumber[-1] == 'J':
                self.score += 10
            elif cardnumber[-1] == 'Q':
                self.score += 10
            elif cardnumber[-1] == 'K':
                self.score += 10
            elif cardnumber[-1] == 'A':
                if self.score + 11 > 21:
                    self.score += 1
                elif self.score + 11 <=21:
                    self.score += 11
        if self.score < 17:
            if self.card3:
                if self.card4:
                    if self.card5:
                        self.card6 = random.choice(Deck.deck)
                        self.cards.append(self.card6)
                        Deck.deck.remove(self.card6)
                    else:
                        self.card5 = random.choice(Deck.deck)
                        self.cards.append(self.card5)
                        Deck.deck.remove(self.card5)
                else:
                    self.card4 = random.choice(Deck.deck)
                    self.cards.append(self.card4)
                    Deck.deck.remove(self.card4)
            else:
                self.card3 = random.choice(Deck.deck)
                self.cards.append(self.card3)
                Deck.deck.remove(self.card3)
    
    def card_surf1(self, screen):
        self.screen = screen
        self.player_score()
        
        for card in self.dcards:
            if self.dcards.index(card) != 1:
                self.screen = screen
                card_i = mcf.Card_Display(self.screen, card, (self.dcards.index(card)*200 + 200), 200)
                card_i.blitme_card()
                card_i.blitme_details()
                    
            else:
                self.screen = screen
                self.screen_rect = screen.get_rect()

                self.image = pygame.image.load('images/cardback.png')
                self.rect = self.image.get_rect()
                self.rect.centerx = self.screen_rect.left + self.dcards.index(card)*200 + 200
                self.rect.centery = self.screen_rect.top + 200

                self.screen.blit(self.image, self.rect)
                    
    def card_surf2(self, screen):
        for card in self.dcards:
            self.screen = screen
            card_i = mcf.Card_Display(self.screen, card, (self.dcards.index(card)*200 + 200), 200)
            card_i.blitme_card()
            card_i.blitme_details()
        
    def deal(self, Deck):
        self.cards = []
        self.card1 = random.choice(Deck.deck)
        Deck.deck.remove(self.card1)
        self.card2 = random.choice(Deck.deck)
        Deck.deck.remove(self.card2)
        self.cards = [self.card1, self.card2]
        
        self.dcard1 = {'suit': None, 'type': None}
        self.dcard2 = {'suit': None, 'type': None}
        self.dcard3 = {'suit': None, 'type': None}
        self.dcard4 = {'suit': None, 'type': None}
        self.dcard5 = {'suit': None, 'type': None}
        self.dcard6 = {'suit': None, 'type': None}
        
        # detailed cards
        self.dcards = [self.dcard1, self.dcard2]
        
        self.card3 = False
        self.card4 = False
        self.card5 = False
        self.card6 = False
        
    def organize(self):
        # Show the cards, excluding the dealers 2nd card
        if self.card6:
            self.cards = [self.card1, self.card2, self.card3, self.card4, self.card5, self.card6]
        elif self.card5:
            self.cards = [self.card1, self.card2, self.card3, self.card4, self.card5]
        elif self.card4:
            self.cards = [self.card1, self.card2, self.card3, self.card4]
        elif self.card3:
            self.cards = [self.card1, self.card2, self.card3]
        else:
            self.cards = [self.card1, self.card2]
            
        if len(self.cards) == 2:
            self.dcards = [self.dcard1, self.dcard2]
        elif len(self.cards) == 3:
            self.dcards = [self.dcard1, self.dcard2, self.dcard3]
        elif len(self.cards) == 4:
            self.dcards = [self.dcard1, self.dcard2, self.dcard3, self.dcard4]
        elif len(self.cards) == 5:
            self.dcards = [self.dcard1, self.dcard2, self.dcard3, self.dcard4, self.dcard5]
        elif len(self.cards) == 6:
            self.dcards = [self.dcard1, self.dcard2, self.dcard3, self.dcard4, self.dcard5, self.dcard6]
            
        for i in range(0, len(self.cards)):
            if 'hearts' in self.cards[i]:
                self.dcards[i]['suit'] = 'hearts'
            elif 'clubs' in self.cards[i]:
                self.dcards[i]['suit'] = 'clubs'
            elif 'spades' in self.cards[i]:
                self.dcards[i]['suit'] = 'spades'
            elif 'diamonds' in self.cards[i]:
                self.dcards[i]['suit'] = 'diamonds'
                
            if 'A' in self.cards[i]:
                self.dcards[i]['type'] = 'A'
            elif '2' in self.cards[i]:
                self.dcards[i]['type'] = '2'
            elif '3' in self.cards[i]:
                self.dcards[i]['type'] = '3'
            elif '4' in self.cards[i]:
                self.dcards[i]['type'] = '4'
            elif '5' in self.cards[i]:
                self.dcards[i]['type'] = '5'
            elif '6' in self.cards[i]:
                self.dcards[i]['type'] = '6'
            elif '7' in self.cards[i]:
                self.dcards[i]['type'] = '7'
            elif '8' in self.cards[i]:
                self.dcards[i]['type'] = '8'
            elif '9' in self.cards[i]:
                self.dcards[i]['type'] = '9'
            elif 'T' in self.cards[i]:
                self.dcards[i]['type'] = 'T'
            elif 'J' in self.cards[i]:
                self.dcards[i]['type'] = 'J'
            elif 'Q' in self.cards[i]:
                self.dcards[i]['type'] = 'Q'
            elif 'K' in self.cards[i]:
                self.dcards[i]['type'] = 'K'
                
 
        
                
    def player_score(self):
        # Show the dealers score
        self.score = 0
        for cardnumber in self.cards:
            if cardnumber[-1] == '2':
                self.score += 2
            elif cardnumber[-1] == '3':
                self.score += 3
            elif cardnumber[-1] == '4':
                self.score += 4
            elif cardnumber[-1] == '5':
                self.score += 5
            elif cardnumber[-1] == '6':
                self.score += 6
            elif cardnumber[-1] == '7':
                self.score += 7
            elif cardnumber[-1] == '8':
                self.score += 8
            elif cardnumber[-1] == '9':
                self.score += 9
            elif cardnumber[-1] == 'T':
                self.score += 10
            elif cardnumber[-1] == 'J':
                self.score += 10
            elif cardnumber[-1] == 'Q':
                self.score += 10
            elif cardnumber[-1] == 'K':
                self.score += 10
            elif cardnumber[-1] == 'A':
                if self.score + 11 > 21:
                    self.score += 1
                elif self.score + 11 <=21:
                    self.score += 11
        return self.score
        

    def score_disp(self, screen):
        score = self.player_score()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.display = myfont2.render(str(score), False, (0, 0, 0))
        self.rect = self.display.get_rect()
        self.rect.centery = self.screen_rect.top + 200
        self.rect.left = self.screen_rect.left + 10

        self.screen.blit(self.display, self.rect)
        
class Player():
    # Establish each player
    
    def __init__(self, Deck, chips=100):
        self.card1 = random.choice(Deck.deck)
        Deck.deck.remove(self.card1)
        self.card2 = random.choice(Deck.deck)
        Deck.deck.remove(self.card2)
        
        self.score = 0
        self.chips = chips
        
        
        self.cards = [self.card1, self.card2]
        
        self.dcard1 = {'suit': None, 'type': '0'}
        self.dcard2 = {'suit': None, 'type': '0'}
        self.dcard3 = {'suit': None, 'type': '0'}
        self.dcard4 = {'suit': None, 'type': '0'}
        self.dcard5 = {'suit': None, 'type': '0'}
        self.dcard6 = {'suit': None, 'type': '0'}
        
        # detailed cards
        self.dcards = []
        
        self.card3 = False
        self.card4 = False
        self.card5 = False
        self.card6 = False
        
    def deal(self, Deck):
        self.cards = []
        self.card1 = random.choice(Deck.deck)
        Deck.deck.remove(self.card1)
        self.card2 = random.choice(Deck.deck)
        Deck.deck.remove(self.card2)
        self.cards = [self.card1, self.card2]
        
        self.dcard1 = {'suit': None, 'type': '0'}
        self.dcard2 = {'suit': None, 'type': '0'}
        self.dcard3 = {'suit': None, 'type': '0'}
        self.dcard4 = {'suit': None, 'type': '0'}
        self.dcard5 = {'suit': None, 'type': '0'}
        self.dcard6 = {'suit': None, 'type': '0'}
        
        # detailed cards
        self.dcards = [self.dcard1, self.dcard2]
        
        self.card3 = False
        self.card4 = False
        self.card5 = False
        self.card6 = False
        
    def hit(self, Deck, screen):
        # add another card to the players hand.
        # Check to see if the player already has a card in that slot.
        if self.card3:
            if self.card4:
                if self.card5:
                    self.card6 = random.choice(Deck.deck)
                    self.cards.append(self.card6)
                    Deck.deck.remove(self.card6)
                else:
                    self.card5 = random.choice(Deck.deck)
                    self.cards.append(self.card5)
                    Deck.deck.remove(self.card5)
            else:
                self.card4 = random.choice(Deck.deck)
                self.cards.append(self.card4)
                Deck.deck.remove(self.card4)
        else:
            self.card3 = random.choice(Deck.deck)
            self.cards.append(self.card3)
            Deck.deck.remove(self.card3)
            
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.hit_display = myfont2.render('HIT!', False, (0, 0, 0))
        self.hit_rect = self.hit_display.get_rect()
        self.hit_rect.centerx = self.screen_rect.centerx
        self.hit_rect.bottom = self.screen_rect.bottom - 10
        self.screen.blit(self.hit_display, self.hit_rect)
        
    def stay(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stay_display = myfont2.render('STAY!', False, (0, 0, 0))
        self.stay_rect = self.stay_display.get_rect()
        self.stay_rect.centerx = self.screen_rect.centerx
        self.stay_rect.bottom = self.screen_rect.bottom - 10
        self.screen.blit(self.stay_display, self.stay_rect)
        
    def card_surf(self, screen):
        self.screen = screen
        self.player_score()
        for card in self.dcards:
            self.screen = screen
            card_i = mcf.Card_Display(self.screen, card, (self.dcards.index(card)*200 + 200), 600)
            card_i.blitme_card()
            card_i.blitme_details()
            
            
        
        
    def organize(self):
        # show each card that the player has. 
        # iterate through to see how many cards the player has.
        if self.card6:
            self.cards = [self.card1, self.card2, self.card3, self.card4, self.card5, self.card6]
        elif self.card5:
            self.cards = [self.card1, self.card2, self.card3, self.card4, self.card5]
        elif self.card4:
            self.cards = [self.card1, self.card2, self.card3, self.card4]
        elif self.card3:
            self.cards = [self.card1, self.card2, self.card3]
        else:
            self.cards = [self.card1, self.card2]
            
        if len(self.cards) == 2:
            self.dcards = [self.dcard1, self.dcard2]
        elif len(self.cards) == 3:
            self.dcards = [self.dcard1, self.dcard2, self.dcard3]
        elif len(self.cards) == 4:
            self.dcards = [self.dcard1, self.dcard2, self.dcard3, self.dcard4]
        elif len(self.cards) == 5:
            self.dcards = [self.dcard1, self.dcard2, self.dcard3, self.dcard4, self.dcard5]
        elif len(self.cards) == 6:
            self.dcards = [self.dcard1, self.dcard2, self.dcard3, self.dcard4, self.dcard5, self.dcard6]
            
        for i in range(0, len(self.cards)):
            if 'hearts' in self.cards[i]:
                self.dcards[i]['suit'] = 'hearts'
            elif 'clubs' in self.cards[i]:
                self.dcards[i]['suit'] = 'clubs'
            elif 'spades' in self.cards[i]:
                self.dcards[i]['suit'] = 'spades'
            elif 'diamonds' in self.cards[i]:
                self.dcards[i]['suit'] = 'diamonds'
                
            if 'A' in self.cards[i]:
                self.dcards[i]['type'] = 'A'
            elif '2' in self.cards[i]:
                self.dcards[i]['type'] = '2'
            elif '3' in self.cards[i]:
                self.dcards[i]['type'] = '3'
            elif '4' in self.cards[i]:
                self.dcards[i]['type'] = '4'
            elif '5' in self.cards[i]:
                self.dcards[i]['type'] = '5'
            elif '6' in self.cards[i]:
                self.dcards[i]['type'] = '6'
            elif '7' in self.cards[i]:
                self.dcards[i]['type'] = '7'
            elif '8' in self.cards[i]:
                self.dcards[i]['type'] = '8'
            elif '9' in self.cards[i]:
                self.dcards[i]['type'] = '9'
            elif 'T' in self.cards[i]:
                self.dcards[i]['type'] = 'T'
            elif 'J' in self.cards[i]:
                self.dcards[i]['type'] = 'J'
            elif 'Q' in self.cards[i]:
                self.dcards[i]['type'] = 'Q'
            elif 'K' in self.cards[i]:
                self.dcards[i]['type'] = 'K'

                
                
                
    def player_score(self):
        # Get the players score by adding the value of each card
        self.score = 0
        for cardnumber in self.cards:
            if cardnumber[-1] == '2':
                self.score += 2
            elif cardnumber[-1] == '3':
                self.score += 3
            elif cardnumber[-1] == '4':
                self.score += 4
            elif cardnumber[-1] == '5':
                self.score += 5
            elif cardnumber[-1] == '6':
                self.score += 6
            elif cardnumber[-1] == '7':
                self.score += 7
            elif cardnumber[-1] == '8':
                self.score += 8
            elif cardnumber[-1] == '9':
                self.score += 9
            elif cardnumber[-1] == 'T':
                self.score += 10
            elif cardnumber[-1] == 'J':
                self.score += 10
            elif cardnumber[-1] == 'Q':
                self.score += 10
            elif cardnumber[-1] == 'K':
                self.score += 10
            elif cardnumber[-1] == 'A':
                if self.score + 11 > 21:
                    self.score += 1
                elif self.score + 11 <=21:
                    self.score += 11
        return self.score
        
        
    def win_chips(self, chips_won):
        self.chips += chips_won
        
    def bet_chips(self, chips_bet):
        self.chips -= chips_bet

    def chip_count(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.display = myfont2.render('Chip Count: ' + str(self.chips), False, (0, 0, 0))
        self.rect = self.display.get_rect()
        self.rect.left = self.screen_rect.left + 10
        self.rect.bottom = self.screen_rect.bottom - 10

        self.screen.blit(self.display, self.rect)
        
    def score_disp(self, screen):
        score = self.player_score()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.display = myfont2.render(str(score), False, (0, 0, 0))
        self.rect = self.display.get_rect()
        self.rect.centery = self.screen_rect.top + 600
        self.rect.left = self.screen_rect.left + 10

        self.screen.blit(self.display, self.rect)
    
    
    
    
    


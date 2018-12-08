import pygame
import random
import os

class Deck():
    
    def __init__(self, number_of_decks=1):
        self.number_decks = number_of_decks
        card_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        suits = ['diamonds', 'clubs', 'spades', 'hearts']

        self.deck = []
        
        for suit in suits:
            for card_number in card_numbers:
                self.deck.append(suit + card_number)
                
class Dealer():
    
    def __init__(self, Deck):
        self.card1 = random.choice(Deck.deck)
        Deck.deck.remove(self.card1)
        self.card2 = random.choice(Deck.deck)
        Deck.deck.remove(self.card2)
        
        self.score = 0
        
        self.card3 = False
        self.card4 = False
        self.card5 = False
        self.card6 = False
        
    def hit(self, Deck):
        if self.card3:
            if self.card4:
                if self.card5:
                    self.card6 = random.choice(Deck.deck)
                    Deck.deck.remove(self.card6)
                else:
                    self.card5 = random.choice(Deck.deck)
                    Deck.deck.remove(self.card5)
            else:
                self.card4 = random.choice(Deck.deck)
                Deck.deck.remove(self.card4)
        else:
            self.card3 = random.choice(Deck.deck)
            Deck.deck.remove(self.card3)
            
    def show_cards(self):
        
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
        
        print('Cards in hand: ')
        for card in self.cards:
            if card == self.card2:
                continue
            else:
                print(card)
                
    def show_cards_final(self):
        
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
        
        print('Cards in hand: ')
        for card in self.cards:
            if card == self.card2:
                continue
            else:
                print(card)
                
    def show_score(self):
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
                        
        print(self.score)
            
        
class Player():
    
    def __init__(self, Deck):
        self.card1 = random.choice(Deck.deck)
        Deck.deck.remove(self.card1)
        self.card2 = random.choice(Deck.deck)
        Deck.deck.remove(self.card2)
        
        self.score = 0
        
        self.card3 = False
        self.card4 = False
        self.card5 = False
        self.card6 = False
        
    def hit(self, Deck):
        if self.card3:
            if self.card4:
                if self.card5:
                    self.card6 = random.choice(Deck.deck)
                    Deck.deck.remove(self.card6)
                else:
                    self.card5 = random.choice(Deck.deck)
                    Deck.deck.remove(self.card5)
            else:
                self.card4 = random.choice(Deck.deck)
                Deck.deck.remove(self.card4)
        else:
            self.card3 = random.choice(Deck.deck)
            Deck.deck.remove(self.card3)
            
    def show_cards(self):
        
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
        
        print('Cards in hand: ')
        for card in self.cards:
            print(card)
            
    def show_score(self):
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
                        
        print(self.score)

        
        

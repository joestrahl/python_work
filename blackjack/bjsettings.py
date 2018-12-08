import sys
import random
import pygame


class Settings():
    """Stores all settings for blackjack"""
    
    def __init__(self, player_number = 1, deck_number = 1, screen_width = 1200, screen_height = 800):
        # Initializes the game settings
        # Screen Settings
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.deck = deck_number
        self.bg_color = (178, 255, 102)
        self.players = []
        
        for i in range(0, player_number):
            self.players.append('new_player' + str(i))
 
        
    

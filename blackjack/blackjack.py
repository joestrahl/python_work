import random
import pygame as pg
import os
import bjfunctions as bjf
import sys
import bjsettings as bjs
import bjlogic as bjl
from intro_screen import Intro
from time import sleep
from player_select import Player_Select
import main_card_functions as mcf

pg.font.init()
myfont2 = pg.font.SysFont('Arial', 60)

def run_game():
    
    intro = True
    player_select = True
    main_game_loop = True
    current_hand = True
    
    pg.init()
    screen = pg.display.set_mode((1200, 800))
    pg.display.set_caption('Blackjack')
    intro_screen = Intro(screen)
    player_select_screen = Player_Select(screen)
    bust = mcf.Bust_Display(screen)
    win = mcf.Win(screen)
    push = mcf.Push(screen)
    lose = mcf.Lose(screen)
    
 
    
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    intro = False
                
        intro_screen.blitme()
        pg.display.flip()
        sleep(1)
        intro = False
        
    while player_select:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        
        screen.fill((230, 230, 230))
        player_select_screen.blitme()
        pg.display.flip()
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    number_players_game = 1
                    player_select = False
                elif event.key == pg.K_2:
                    number_players_game = 2
                    player_select = False
                elif event.key == pg.K_3:
                    number_players_game = 3
                    player_select = False
                    
                
        
        
        
        
    # Establish number of players and decks
    settings = bjs.Settings(number_players_game, 2)
    # Use number of decks from settings to create the game deck
    gamedeck = bjf.Deck(settings.deck)
    player1_turn = True
    
    
    if number_players_game == 1:
        player1 = bjf.Player(gamedeck)
        player1.organize()
    elif number_players_game == 2:
        player1 = bjf.Player(gamedeck)
        player2 = bjf.Player(gamedeck)
        player1.organize()
        player2.organize()
    elif number_players_game == 3:
        player1 = bjf.Player(gamedeck)
        player2 = bjf.Player(gamedeck)
        player3 = bjf.Player(gamedeck)
        player1.organize()
        player2.organize()
        player3.organize()
        
    chips = mcf.Chip_Display(screen, player1)
    dealer = bjf.Dealer(gamedeck)
    dealer.organize()
    bet = 10

    gamedeck = bjf.Deck(settings.deck)
    player_score = mcf.Score_Display(screen, player1)
    dealer_score = mcf.Dealer_Score_Display(screen, dealer)
    while main_game_loop:
        player1_turn = True
        dealer_turn = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        gamedeck = bjf.Deck(2)
        player1.cards = []
        dealer.cards = []
        player1.deal(gamedeck)
        dealer.deal(gamedeck)
        player1.organize()
        dealer.organize()
        screen.fill((120, 200, 120))
 
        
        if number_players_game == 1:
            screen.fill((120, 200, 120))
            player1.card_surf(screen)
            dealer.card_surf1(screen)
            player1.bet_chips(bet)
            player1.score_disp(screen)
            player1.chip_count(screen)
            pg.display.flip()
            
            
            while player1_turn == True:
                screen.fill((120, 200, 120))
                player1.score_disp(screen)
                player1.chip_count(screen)
                player1.card_surf(screen)
                dealer.card_surf1(screen)
                player1.player_score()
                pg.display.flip()
                
                if len(player1.cards) == 2 and player1.score == 21:
                    player1.win_chips(bet*2)
                    win.blitme()
                    player1.score_disp(screen)
                    pg.display.flip()
                    sleep(2)
                    player_turn = False
                    dealer_turn = False
                    
                
                for event in pg.event.get():
                    screen.fill((120, 200, 120))
                    if event.type == pg.QUIT:
                        sys.exit()
                        
                    elif event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            screen.fill((120, 200, 120))
                            player1.card_surf(screen)
                            dealer.card_surf1(screen)
                            player1.hit(gamedeck, screen)
                            player1.organize()
                            player1.chip_count(screen)
                            pg.display.update()
                            pg.display.flip()
                            sleep(1)
                            player1.score_disp(screen)
                            player1.player_score()
                            pg.display.flip()
                            
                            if player1.score < 22:
                                continue
                            elif player1.score >= 22:
                                screen.fill((120, 200, 120))
                                player1.card_surf(screen)
                                player1.player_score()
                                player1.chip_count(screen)
                                dealer.card_surf2(screen)
                                dealer.score_disp(screen)
                                player1.score_disp(screen)
                                bust.blitme()
                                pg.display.update()
                                pg.display.flip()
                                sleep(1)
                                player1_turn = False
                            
                            if player1.score == 21 and len(player1.cards) > 2:
                                dealer_turn = True
                                player1_turn = False
                                
                        if event.key == pg.K_s:
                            dealer_turn = True
                            player1_turn = False
            
            while dealer_turn == True:
                screen.fill((120, 200, 120))
                player1.card_surf(screen)
                player1.player_score()
                player1.chip_count(screen)
                dealer.player_score()
                dealer.score_disp(screen)
                player1.score_disp(screen)
                dealer.card_surf2(screen)
                pg.display.flip()
                dealer.player_score()
                
                while dealer.score < 17:
                    
                    if len(dealer.cards) == 2:
                        sleep(1)
                        
                    screen.fill((120, 200, 120))
                    dealer.hit(gamedeck)
                    dealer.organize()
                    dealer.card_surf2(screen)
                    player1.player_score()
                    dealer.player_score()
                    player1.chip_count(screen)
                    player1.card_surf(screen)
                    player1.score_disp(screen)
                    dealer.score_disp(screen)
                    pg.display.flip()
                    sleep(1)
                
                if dealer.score > 21:
                    player1.win_chips(bet*2)
                    win.blitme()
                    pg.display.flip()
                    sleep(2)
                    dealer_turn = False    
                elif dealer.score == player1.score:
                    player1.win_chips(bet)
                    push.blitme()
                    pg.display.flip()
                    sleep(2)
                    dealer_turn = False
                elif dealer.score < player1.score:
                    player1.win_chips(bet*2)
                    win.blitme()
                    pg.display.flip()
                    sleep(2)
                    dealer_turn = False
                elif dealer.score > player1.score:
                    lose.blitme()
                    pg.display.flip()
                    sleep(2)
                    dealer_turn = False
                        
                
                chips.blitme()
                player1.card_surf(screen)
                pg.display.update()
                pg.display.flip()
                

            pg.display.flip()
        pg.display.flip()
        
run_game()

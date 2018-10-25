#a basic game to learn how to code rock paper scissors.

import random
import time
import os

user = ['rock', 'paper', 'scissors']
computer = ['rock', 'paper', 'scissors']

u_points = 0
c_points = 0
new = 'yes'

print('Rock, Paper, Scissors: Best 3 out of 5!\
\n\nType "Quit" at any time to exit the game.\n')
time.sleep(5)

os.system('cls')

while new == 'yes':
    while u_points < 3 and c_points < 3:
        os.system('cls')
        print(" |S C O R E B O A R D|\n____YOU_______OPP_____\n|         |          |\n|    %d    |    %d     |\n|_________|__________|" % (u_points, c_points))
        t_1 = input("\n\nWhat would you like to throw? \
        \n1. Rock \
        \n2. Paper \
        \n3. Scissors \
        \n(Type the number of your response): ")
    
        if t_1 == 'Quit':
            break
    
        if t_1 == '1':   #Establishing whether you have beaten, tied, or lost
            os.system('cls') #Clear previous
        
            t_2 = random.choice(computer) #The computers choice is random.
        
            if t_2 == 'rock':
                print('Rock')
                time.sleep(1)
                print('vs')
                time.sleep(1)
                print(t_2.title())
                time.sleep(1)
            
                print('\nCaught between a rock and a... The score remains ' \
                + str(u_points) + ' to ' + str(c_points)) 
                time.sleep(3)
            
            elif t_2 == 'paper':
                c_points += 1
                print('Rock')
                time.sleep(1)
                print('vs')
                time.sleep(1)
                print(t_2.title())
                time.sleep(1)
                print("\nYou've been smothered! The score is " \
                + str(u_points) + ' to ' + str(c_points))
                time.sleep(3)
            
            elif t_2 == 'scissors':
                u_points += 1
                print('Rock')
                time.sleep(1)
                print('vs')
                time.sleep(1)
                print(t_2.title())
                time.sleep(1)
                print('\nYou crushed him! The score is ' + str(u_points) + \
                ' to ' + str(c_points))
                time.sleep(3)

        elif t_1 == '2':   #Establishing whether you have beaten, tied, or lost
            os.system('cls') #Clear previous
        
            t_2 = random.choice(computer) #The computers choice is random.
        
            if t_2 == 'rock':
                u_points +=1
                print('Paper')
                time.sleep(1)
                print('vs')
                time.sleep(1)
                print(t_2.title())
                time.sleep(1)
                print('\nYou smothered him! The score is ' + str(u_points)\
                + ' to ' + str(c_points)) 
                time.sleep(3)
            
            elif t_2 == 'paper':
                print('Paper')
                time.sleep(1)
                print('vs')
                time.sleep(1)
                print(t_2.title())
                time.sleep(1)
                print('\nFlat on flat! The score remains ' + str(u_points) + \
                ' to ' + str(c_points))
                time.sleep(3)
            
            elif t_2 == 'scissors':
                c_points += 1
                print('Paper')
                time.sleep(1)
                print('vs')
                time.sleep(1)
                print(t_2.title())
                time.sleep(1)
                print('\nSliced and diced! The score is ' + str(u_points) + \
                ' to ' + str(c_points))   
                time.sleep(3) 
            
        elif t_1 == '3':#Establishing whether you have beaten, tied, or lost
            os.system('cls') #Clear previous
        
            t_2 = random.choice(computer) #The computers choice is random.
        
            if t_2 == 'rock':
                c_points += 1
                print('Scissors')
                time.sleep(1)
                print('vs')
                time.sleep(1)
                print(t_2.title())
                time.sleep(1)
                print('\nYou were crushed! The score is ' + str(u_points) + \
                ' to ' + str(c_points)) 
                time.sleep(3)
            
            elif t_2 == 'paper':
                u_points += 1
                print('Scissors')
                time.sleep(1)
                print('vs')
                time.sleep(1)
                print(t_2.title())
                time.sleep(1)
                print('\nYou sliced up their paper! The score is ' + str(u_points) + \
                ' to ' + str(c_points))
                time.sleep(3)
                
            elif t_2 == 'scissors':
                print('Scissors')
                time.sleep(1)
                print('vs')
                time.sleep(1)
                print(t_2.title())
                time.sleep(1)
                print('\nClang! Ding! The score remains ' + str(u_points) + \
                ' to ' + str(c_points))
                time.sleep(3)

        os.system('cls')

        if u_points > c_points:
            print('You won! \n\nFinal Score: ' + str(u_points) + ' to ' \
            + str(c_points))
        else:
            print('You lost!\n\nFinal Score: ' + str(u_points) + ' to ' \
            + str(c_points))

    new = input("\nWant to play again? ('yes' or 'no'): ")
    
    if new == 'yes':
        u_points = 0
        c_points = 0


    if new == 'no':
        break

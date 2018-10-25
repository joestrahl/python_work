import random
import os
import sys


"""A game that allow the user to try to guess a number"""
"""The user will have 5 tries to narrow it down between 1 and 50"""

user_input = int(input('Pick a number between 1 and 50: '))

user_count = 4
past_guesses = []
random_number = int(random.choice(range(1, 51)))

while user_count > 0:
    if user_input == random_number:
        os.system('cls')
        print('You\'ve won! The correct guess was: ' + str(random_number))
        ng = input('Play again? (y/n): ')
        if ng == 'y':
            user_count = 5
            random_number = int(random.choice(range(1,51)))
        elif ng == 'n':
            break

    elif user_input <= random_number:
        user_count -= 1
        past_guesses.append(user_input)
        print('Past Guesses:')
        for guess in past_guesses:
            print(guess)
        user_input = int(input('Your guess of ' + str(user_input) + 
            ' was too low, try again: '))
       
    elif user_input >= random_number:
        user_count -= 1
        past_guesses.append(user_input)
        print('Past Guesses: ')
        for guess in past_guesses:
            print(guess)
        user_input = int(input('your guess of ' + str(user_input) + 
            ' was too high, try again: '))
            

       

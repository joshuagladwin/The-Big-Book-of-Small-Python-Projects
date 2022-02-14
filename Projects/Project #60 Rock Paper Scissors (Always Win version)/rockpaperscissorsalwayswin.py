"""Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
The classic hand game of luck.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, game"""

import random, time, sys

print('''Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

# These variables keep track of the number of wins.
wins = 0


while True:  # Main game loop.
    while True:  # Keep asking until player enters R, P, S, or Q.
        print(f'{wins} Wins, 0 Losses, 0 Ties')
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        player_move = input('> ').upper()
        if player_move == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if player_move == 'R' or player_move == 'P' or player_move == 'S':
            break
        else:
            print('Type one of R, P, S, or Q.')

    # Display what the player chose:
    if player_move == 'R':
        print('ROCK versus...')
    elif player_move == 'P':
        print('PAPER versus...')
    elif player_move == 'S':
        print('SCISSORS versus...')

    # Count to three with dramatic pauses:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Display what the computer chose:
    if player_move == 'R':
        print('SCISSORS')
    elif player_move == 'P':
        print('ROCK')
    elif player_move == 'S':
        print('PAPER')

    time.sleep(0.5)

    print('You win!')
    wins = wins + 1
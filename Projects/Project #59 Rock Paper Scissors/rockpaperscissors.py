"""Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
The classic hand game of luck.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: short, game"""

import random, time, sys

print('''Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com
- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # Main game loop.
    while True:  # Keep asking until player enters R, P, S, or Q.
        print(f'{wins} Wins, {losses} Losses, {ties} Ties')
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
        player_move = 'ROCK'
    elif player_move == 'P':
        print('PAPER versus...')
        player_move = 'PAPER'
    elif player_move == 'S':
        print('SCISSORS versus...')
        player_move = 'SCISSORS'

    # Count to three with dramatic pauses:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Display what the computer chose:
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'ROCK'
    if random_number == 2:
        computer_move = 'PAPER'
    if random_number == 3:
        computer_move = 'SCISSORS'
    print(computer_move)
    time.sleep(0.5)

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It\'s a tie!')
        ties = ties + 1
    elif player_move == 'ROCK' and computer_move == 'SCISSORS':
        print('You win!')
        wins = wins + 1
    elif player_move == 'PAPER' and computer_move == 'ROCK':
        print('You win!')
        wins = wins + 1
    elif player_move == 'SCISSORS' and computer_move == 'PAPER':
        print('You win!')
        wins = wins + 1
    elif player_move == 'ROCK' and computer_move == 'PAPER':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'PAPER' and computer_move == 'SCISSORS':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'SCISSORS' and computer_move == 'PAPER':
        print('You lose!')
        losses = losses + 1

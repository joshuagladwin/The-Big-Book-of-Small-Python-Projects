"""The Royal Game of Ur, by Al Sweigart al@inventwithpython.com
A 5,000 year old board game from Mesopotamia. Two players knock each
other back as they race for the goal.
More info https://en.wikipedia.org/wiki/Royal_Game_of_Ur
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: large, board game, game, two-player
"""

import random, sys

X_PLAYER = 'X'
O_PLAYER = 'O'
EMPTY = ' '

# Set up constants for the space labels:
X_HOME = 'x_home'
O_HOME = 'o_home'
X_GOAL = 'x_goal'
O_GOAL = 'o_goal'

# The spaces in left to right, top to bottom order:
ALL_SPACES = 'hgfetsijklmnopdcbarq'
X_TRACK = 'HefghijklmnopstG'  # (H stands for Home, G stands for Goal.)
O_TRACK = 'HabcdijklmnopqrG'

FLOWER_SPACES = ('h', 't', 'l', 'd', 'r')

BOARD_TEMPLATE = """
                   {}           {}
                   Home              Goal
                     v                 ^
+-----+-----+-----+--v--+           +--^--+-----+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****h|    g|    f|    e|           |****t|    s|
+--v--+-----+-----+-----+-----+-----+-----+--^--+
|     |     |     |*****|     |     |     |     |
|  {}  >  {}  >  {}  >* {} *>  {}  >  {}  >  {}  >  {}  |
|    i|    j|    k|****l|    m|    n|    o|    p|
+--^--+-----+-----+-----+-----+-----+-----+--v--+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****d|    c|    b|    a|           |****r|    q|
+-----+-----+-----+--^--+           +--v--+-----+
                     ^                 v
                   Home              Goal
                   {}           {}
"""


def main():
    print('''The Royal Game of Ur, by Al Sweigart

This is a 5,000 year old game. Two players must move their tokens
from their home to their goal. On your turn you flip four coins and can
move one token a number of spaces equal to the heads you got.

Ur is a racing game; the first player to move all seven of their tokens
to their goal wins. To do this, tokens must travel from their home to
their goal:

            X Home      X Goal
              v           ^
+---+---+---+-v-+       +-^-+---+
|v<<<<<<<<<<<<< |       | ^<|<< |
|v  |   |   |   |       |   | ^ |
+v--+---+---+---+---+---+---+-^-+
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^ |
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>v |
+^--+---+---+---+---+---+---+-v-+
|^  |   |   |   |       |   | v |
|^<<<<<<<<<<<<< |       | v<<<< |
+---+---+---+-^-+       +-v-+---+
              ^           v
            O Home      O Goal

If you land on an opponent's token in the middle track, it gets sent
back home. The **flower** spaces let you take another turn. Tokens in
the middle flower space are safe and cannot be landed on.''')
    input('Press Enter to begin...')

    game_board = get_new_board()
    turn = O_PLAYER
    while True:  # Main game loop.
        # Set up some variables for this turn:
        if turn == X_PLAYER:
            opponent = O_PLAYER
            home = X_HOME
            track = X_TRACK
            goal = X_GOAL
            opponent_home = O_HOME
        elif turn == O_PLAYER:
            opponent = X_PLAYER
            home = O_HOME
            track = O_TRACK
            goal = O_GOAL
            opponent_home = X_HOME

        display_board(game_board)

        input(f'It is {turn}\'s turn. Press Enter to flip...')

        flip_tally = 0
        print('Flips: ', end='')
        for i in range(4):  # Flip 4 coins.
            result = random.randint(0, 1)
            if result == 0:
                print('T', end='')  # Tails
            else:
                print('H', end='')  # Heads
            if i != 3:
                print('-', end='')  # Print separator.
            flip_tally += result
        print('  ', end='')

        if flip_tally == 0:
            input('You lose a turn. Press Enter to continue...')
            turn = opponent  # Swap turns to the other player.
            continue

        # Ask the player for their move:
        valid_moves = get_valid_moves(game_board, turn, flip_tally)

        if valid_moves == []:
            print('There are no possible moves, so you lose a turn.')
            input('Press Enter to continue...')
            turn = opponent  # Swap turns to the other player.
            continue

        while True:
            print(f'Select move {flip_tally} spaces: ', end='')
            print(' '.join(valid_moves) + ' quit')
            move = input('> ').lower()

            if move == 'quit':
                print('Thanks for playing!')
                sys.exit()
            if move in valid_moves:
                break  # Exit the loop when a valid move is selected.

            print('That is not a valid move.')

        # Perform the selected move on the board:
        if move == 'home':
            # Subtract tokens at home if moving from home:
            game_board[home] -= 1
            next_track_space_index = flip_tally
        else:
            game_board[move] = EMPTY  # Set the "from" space to empty.
            next_track_space_index = track.index(move) + flip_tally

        moving_onto_goal = next_track_space_index == len(track) - 1
        if moving_onto_goal:
            game_board[goal] += 1
            # Check if the player has won:
            if game_board[goal] == 7:
                display_board(game_board)
                print(f'{turn} has won the game!')
                print('Thanks for playing!')
                sys.exit()
        else:
            next_board_space = track[next_track_space_index]
            # Check if the opponent has a tile there:
            if game_board[next_board_space] == opponent:
                game_board[opponent_home] += 1

            # Set the "to" space to the player's token:
            game_board[next_board_space] = turn

        # Check if the player landed on a flower space and can go again:
        if next_board_space in FLOWER_SPACES:
            print(f'{turn} landed on a flower space and goes again.')
            input('Press Enter to continue...')
        else:
            turn = opponent  # Swap turns to the other player.

def get_new_board():
    """
    Returns a dictionary that represents the state of the board. The
    keys are strings of the space labels, the values are X_PLAYER,
    O_PLAYER, or EMPTY. There are also counters for how many tokens are
    at the home and goal of both players.
    """
    board = {X_HOME: 7, X_GOAL: 0, O_HOME: 7, O_GOAL: 0}
    # Set each space as empty to start:
    for space_label in ALL_SPACES:
        board[space_label] = EMPTY
    return board


def display_board(board):
    """Display the board on the screen."""
    # "Clear" the screen by printing many newlines, so the old
    # board isn't visible anymore.
    print('\n' * 60)

    x_home_tokens = ('X' * board[X_HOME]).ljust(7, '.')
    x_goal_tokens = ('X' * board[X_GOAL]).ljust(7, '.')
    o_home_tokens = ('O' * board[O_HOME]).ljust(7, '.')
    o_goal_tokens = ('O' * board[O_GOAL]).ljust(7, '.')

    # Add the strings that should populate BOARD_TEMPLATE in order,
    # going from left to right, top to bottom.
    spaces = []
    spaces.append(x_home_tokens)
    spaces.append(x_goal_tokens)
    for space_label in ALL_SPACES:
        spaces.append(board[space_label])
    spaces.append(o_home_tokens)
    spaces.append(o_goal_tokens)

    print(BOARD_TEMPLATE.format(*spaces))


def get_valid_moves(board, player, flip_tally):
    valid_moves = []  # Contains the spaces with tokesn that can move.
    if player == X_PLAYER:
        opponent = O_PLAYER
        track = X_TRACK
        home = X_HOME
    elif player == O_PLAYER:
        opponent = X_PLAYER
        track = O_TRACK
        home = O_HOME

    # Check if the player can move a token from home:
    if board[home] > 0 and board[track[flip_tally]] == EMPTY:
        valid_moves.append('home')

    # Check which spaces have a token the player can move:
    for track_space_index, space in enumerate(track):
        if space == 'H' or space == 'G' or board[space] != player:
            continue
        next_track_space_index = track_space_index + flip_tally
        if next_track_space_index >= len(track):
            # You must flip an exact number of moves onto the goal,
            # otherwise you can't move on the goal.
            continue
        else:
            next_board_space_key = track[next_track_space_index]
            if next_board_space_key == 'G':
                # This token can move off the board:
                valid_moves.append(space)
                continue
        if board[next_board_space_key] in (EMPTY, opponent):
            # If the next space is the protected middle space, you
            # can only move there if it is empty:
            if next_board_space_key == 'l' and board['l'] == opponent:
                continue  # Skip this move, the space is protected.
            valid_moves.append(space)


    return valid_moves

if __name__ == '__main__':
    main()
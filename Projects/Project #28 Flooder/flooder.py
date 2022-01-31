"""Flooder, by Al Sweigart al@inventwithpython.com
A colorful game where you try to fill the board with a single color. Has
a mode for colorblind players.
Inspired by the "Flood It!" Game.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: large, bext, game"""

import random, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext')
    sys.exit()

# Set up the constants:
BOARD_WIDTH = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME = 20

# Constants for the different shapes used in colorblind mode:
HEART = chr(9829)  # Character 9829 is '♥'.
DIAMOND = chr(9830)  # Character 9830 is '♦'.
SPADE = chr(9824)  # Character 9824 is '♠'.
CLUB = chr(9827)  # Character 9827 is '♣'.
BALL = chr(9679)  # Character 9679 is '•.
TRIANGLE = chr(9650)  # Character 9650 is '▲'.

BLOCK = chr(9608)  # Character 9608 is '█'
LEFTRIGHT = chr(9472)  # Character 9472 is '─'
UPDOWN = chr(9474)  # Character 9474 is '│'
DOWNRIGHT = chr(9484)  # Character 9484 is '┌'
DOWNLEFT = chr(9488)  # Character 9488 is '┐'
UPRIGHT = chr(9492)  # Character 9492 is '└'
UPLEFT = chr(9496)  # Character 9496 is '┘'
# A list of chr() codes is at https://inventwithpython.com/chr

# All the color/shape tiles used on the board:
TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2: 'blue',
              3: 'yellow', 4: 'cyan', 5: 'purple'}
COLOR_MODE = 'color mode'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND,
              3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'shape mode'


def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('''Flooder, by Al Sweigart al@inventwithpython.com

Set the upper left color/shape, which fills in all the
adjacent squares of the color/shape. Try to make the
entire board the same color/shape.''')

    print('Do you want to play in colorblind mode? Y/N')
    response = input()
    if response.upper().startswith('Y'):
        display_mode = SHAPE_MODE
    else:
        display_mode = COLOR_MODE

    game_board = get_new_board()
    moves_left = MOVES_PER_GAME

    while True:  # Main game loop.
        display_board(game_board, display_mode)

        print('Moves left:', moves_left)
        player_move = ask_for_player_move(display_mode)
        change_tile(player_move, game_board, 0, 0)
        moves_left -= 1

        if has_won(game_board):
            display_board(game_board, display_mode)
            print('You have won!')
            break
        elif moves_left == 0:
            display_board(game_board, display_mode)
            print('You have run out of moves!')
            break


def get_new_board():
    """Return a dictionary of a new Flood It board."""

    # Keys are (x, y) tuples, values are the tile at that position.
    board = {}

    # Create random colors for the board.
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y,)] = random.choice(TILE_TYPES)

    # Make several tiles the same as their neighbors. This creates groups
    # of the same color/shape.
    for i in range(BOARD_WIDTH * BOARD_HEIGHT):
        x = random.randint(0, BOARD_WIDTH - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board


def display_board(board, display_mode):
    """Display the board on the screen."""
    bext.fg('white')
    # Display the top edge of the board:
    print(DOWNRIGHT + (LEFTRIGHT * BOARD_WIDTH) + DOWNLEFT)

    # Display each row:
    for y in range(BOARD_HEIGHT):
        bext.fg('white')
        if y == 0:  # The first row begins with '>'.
            print('>', end='')
        else:  # Late rows begin with a white vertical line.
            print(UPDOWN, end='')

        # Display each tile in this row:
        for x in range(BOARD_WIDTH):
            bext.fg(COLORS_MAP[board[(x, y)]])
            if display_mode == COLOR_MODE:
                print(BLOCK, end='')
            elif display_mode == SHAPE_MODE:
                print(SHAPES_MAP[board[(x, y)]], end='')

        bext.fg('white')
        print(UPDOWN)  # Rows end with a white vertical line.
    # Display the bottom edge of the board:
    print(UPRIGHT + (LEFTRIGHT * BOARD_WIDTH) + UPLEFT)


def ask_for_player_move(display_mode):
    """Let the player select a color to paint the upper left tile."""
    while True:
        bext.fg('white')
        print('Choose one of ', end='')

        if display_mode == COLOR_MODE:
            bext.fg('red')
            print('(R)ed ', end='')
            bext.fg('green')
            print('(G)reen ', end='')
            bext.fg('blue')
            print('(B)lue ', end='')
            bext.fg('yellow')
            print('(Y)ellow ', end='')
            bext.fg('cyan')
            print('(C)yan ', end='')
            bext.fg('purple')
            print('(P)urple ', end='')
        elif display_mode == SHAPE_MODE:
            bext.fg('red')
            print('(H)eart ', end='')
            bext.fg('green')
            print('(T)riangle ', end='')
            bext.fg('blue')
            print('(D)iamond ', end='')
            bext.fg('yellow')
            print('(B)all ', end='')
            bext.fg('cyan')
            print('(C)lub ', end='')
            bext.fg('purple')
            print('(S)pade ', end='')
        bext.fg('white')
        print('or QUIT:')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if display_mode == COLOR_MODE and response in tuple('RGBYCP'):
            # Return a tile type number based on the response:
            return {'R': 0, 'G': 1, 'B': 2,
                    'Y': 3, 'C': 4, 'P': 5}[response]
        if display_mode == SHAPE_MODE and response in tuple('HTDBCS'):
            # Return a tile type number based on the response:
            return {'H': 0, 'T': 1, 'D': 2,
                    'B': 3, 'C': 4, 'S': 5}[response]


def change_tile(tile_type, board, x, y, char_to_change=None):
    """Change the color/shape of a tile using the recursive flood fill
    algorithm."""
    if x == 0 and y == 0:
        char_to_change = board[(x, y)]
        if tile_type == char_to_change:
            return  # Base Case: Already is the same tile.

    board[(x, y)] = tile_type

    if x > 0 and board[(x - 1, y)] == char_to_change:
        # Recursive Case: Change the left neighbor's tile:
        change_tile(tile_type, board, x - 1, y, char_to_change)
    if y > 0 and board[(x, y - 1)] == char_to_change:
        # Recursive Case: Change the top neighbor's tile:
        change_tile(tile_type, board, x, y - 1, char_to_change)
    if x < BOARD_WIDTH - 1 and board[(x + 1, y)] == char_to_change:
        # Recursive Case: Change the right neighbor's tile:
        change_tile(tile_type, board, x + 1, y, char_to_change)
    if y < BOARD_HEIGHT - 1 and board[(x, y + 1)] == char_to_change:
        # Recursive Case: Change the bottom neighbor's tile:
        change_tile(tile_type, board, x, y + 1, char_to_change)


def has_won(board):
    """Return True if the entire board is one color/shape."""
    tile = board[(0, 0)]

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()

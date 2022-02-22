"""Sliding Tile Puzzle, by Al Sweigart al@inventwithpython.com
Slide the numbered tiles into the correct order.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, puzzle"""

import random, sys

BLANK = '  '  # Note: This string is two spaces, not one.


def main():
    print('''Sliding Tile Puzzle, by Al Sweigart al@inventwithpython.com
    
    Use the WASD keys to move the tiles
    back into their original order:
           1  2  3  4
           5  6  7  8
           9 10 11 12
          13 14 15   ''')
    input('Press Enter to begin...')

    game_board = get_new_puzzle()

    while True:
        display_board(game_board)
        player_move = ask_for_player_move(game_board)
        make_move(game_board, player_move)

        if game_board == get_new_board():
            display_board(game_board)
            print('You won!')
            sys.exit()


def get_new_board():
    """Returns a list of lists that represent a new tile puzzle."""
    return [['1 ', '5 ', '9 ', '13'], ['2 ', '6 ', '10', '14'],
            ['3 ', '7 ', '11', '15'], ['4 ', '8 ', '12', BLANK]]


def display_board(board):
    """Display the given board on the screen."""
    labels = [board[0][0], board[1][0], board[2][0], board[3][0],
              board[0][1], board[1][1], board[2][1], board[3][1],
              board[0][2], board[1][2], board[2][2], board[3][2],
              board[0][3], board[1][3], board[2][3], board[3][3]]
    board_to_draw = """
+------+------+------+------+   
|      |      |      |      |    
|  {}  |  {}  |  {}  |  {}  |    
|      |      |      |      |    
+------+------+------+------+    
|      |      |      |      |    
|  {}  |  {}  |  {}  |  {}  |    
|      |      |      |      |    
+------+------+------+------+    
|      |      |      |      |    
|  {}  |  {}  |  {}  |  {}  |    
|      |      |      |      |    
+------+------+------+------+    
|      |      |      |      |    
|  {}  |  {}  |  {}  |  {}  |    
|      |      |      |      |    
+------+------+------+------+    
""".format(*labels)
    print(board_to_draw)


def find_blank_space(board):
    """Return an (x, y) tuple of the blank space's location."""
    for x in range(4):
        for y in range(4):
            if board[x][y] == '  ':
                return (x, y)


def ask_for_player_move(board):
    """Let the player select a tile to slide."""
    blank_x, blank_y = find_blank_space(board)

    w = 'W' if blank_y != 3 else ' '
    a = 'A' if blank_x != 3 else ' '
    s = 'S' if blank_y != 0 else ' '
    d = 'D' if blank_x != 0 else ' '

    while True:
        print(f'                          ({w})')
        print(f'Enter WASD (or QUIT): ({a}) ({s}) ({d})')

        response = input('> ').upper()
        if response == 'QUIT':
            sys.exit()
        if response in (w + a + s + d).replace(' ', ''):
            return response


def make_move(board, move):
    """Carry out the given move on the given board."""
    # Note: This function assumes that the move is valid.
    b_x, b_y = find_blank_space(board)

    if move == 'W':
        board[b_x][b_y], board[b_x][b_y+1] = board[b_x][b_y+1], board[b_x][b_y]
    if move == 'A':
        board[b_x][b_y], board[b_x+1][b_y] = board[b_x+1][b_y], board[b_x][b_y]
    if move == 'S':
        board[b_x][b_y], board[b_x][b_y-1] = board[b_x][b_y-1], board[b_x][b_y]
    if move == 'D':
        board[b_x][b_y], board[b_x-1][b_y] = board[b_x-1][b_y], board[b_x][b_y]


def make_random_move(board):
    """Perform a slide in a random direction."""
    blank_x, blank_y = find_blank_space(board)
    valid_moves = []
    if blank_y != 3:
        valid_moves.append('W')
    if blank_x != 3:
        valid_moves.append('A')
    if blank_y != 0:
        valid_moves.append('S')
    if blank_x != 0:
        valid_moves.append('D')

    make_move(board, random.choice(valid_moves))


def get_new_puzzle(moves=200):
    """Get a new puzzle by making random slides from a solved state."""
    board = get_new_board()

    for i in range(moves):
        make_random_move(board)
    return board


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()

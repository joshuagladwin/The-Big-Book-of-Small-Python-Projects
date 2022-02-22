"""Twenty Forty-Eight, by Al Sweigart al@inventwithpython.com
A sliding tile game to combine exponentially-increasing numbers.
Inspired by Gabriele Cirulli's 2048, which is a clone of Veewo Studios'
1024, which in turn is a clone of the Threes! game.
More info at https://en.wikipedia.org/wiki/2048_(video_game)
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, puzzle"""

import random, sys

# Set up the constants:
BLANK = ''  # A value that represents a blank space on the board.


def main():
    print('''Twenty Forty-Eight, by Al Sweigart al@inventwithpython.com

Slide all the tiles on the board in one of four directions. Tiles with
like numbers will combine into larger-numbered tiles. A new 2 tile is
added to the board on each move. You win if you can create a 2048 tile.
You lose if the board fills up the tiles before then.''')
    input('Press Enter to begin...')

    game_board = get_new_board()

    while True:  # Main game loop.
        draw_board(game_board)
        print(f'Score: {get_score(game_board)}')
        player_move = ask_for_player_move()
        game_board = make_move(game_board, player_move)
        add_two_to_board(game_board)

        if is_full(game_board):
            draw_board(game_board)
            print('Game Over - Thanks for playing!')
            sys.exit()


def get_new_board():
    """Returns a new data structure that represents a board.

    It's a dictionary with keys of (x, y) tuples and values of the tile
    at that space. The tile is either a power-of-two integer or BLANK.
    The coordinates are laid out as:
       X0 1 2 3
       Y+-+-+-+-+
       0| | | | |
       +-+-+-+-+
       1| | | | |
       +-+-+-+-+
       2| | | | |
       +-+-+-+-+
       3| | | | |
       +-+-+-+-+"""

    new_board = {}  # Contains the board data structure to be returned.
    # Loop over every possible space and set all the tiles to blank:
    for x in range(4):
        for y in range(4):
            new_board[(x, y)] = BLANK

    # Pick two random spaces for the two starting 2s:
    starting_twos_placed = 0  # The number of starting spaces picked.
    while starting_twos_placed < 2:  # Repeat for duplicated spaces.
        random_space = (random.randint(0, 3), random.randint(0, 3))
        # Make sure the randomly selected space isn't already taken:
        if new_board[random_space] == BLANK:
            new_board[random_space] = 2
            starting_twos_placed = starting_twos_placed + 1

    return new_board


def draw_board(board):
    """Draws the board data structure on the screen."""

    # Go through each possible space left to right, top to bottom, and
    # create a list of what each space's label should be.
    labels = []  # A list of strings for the number/blank for that tile.
    for y in range(4):
        for x in range(4):
            tile = board[(x, y)]  # Get the tile at this space.
            # Make sure the label is 5 spaces long:
            label_for_this_tile = str(tile).center(5)
            labels.append(label_for_this_tile)

    # The {} are replaced with the label for that tile:
    print("""
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
""".format(*labels))


def get_score(board):
    """Returns the sum of all the tiles on the board data structure."""
    score = 0
    # Loop over every space and add the tile to the score:
    for x in range(4):
        for y in range(4):
            # Only add non-blank tiles to the score:
            if board[(x, y)] != BLANK:
                score = score + board[(x, y)]
    return score


def combine_tiles_in_column(column):
    """The column is a list of four tile. Index 0 is the "bottom" of
    the column, and tiles are pulled "down" and combine if they are the
    same. For example, combineTilesInColumn([2, BLANK, 2, BLANK])
    returns [4, BLANK, BLANK, BLANK]."""

    # Copy only the numbers (not BLANKS) from column to combined_tiles
    combined_tiles = []  # A list of non-blank tiles in column.
    for i in range(4):
        if column[i] != BLANK:
            combined_tiles.append(column[i])

    # Keep adding blanks until there are 4 tiles:
    while len(combined_tiles) < 4:
        combined_tiles.append(BLANK)

    # Combine numbers if the one "above" it is the same, and double it.
    for i in range(3):  # Skip index 3, it's the topmost space.
        if combined_tiles[i] == combined_tiles[i + 1]:
            combined_tiles[i] *= 2  # Double the number in the tile.
            # Move the tiles above it down one space:
            for above_index in range(i + 1, 3):
                combined_tiles[above_index] = combined_tiles[above_index + 1]
            combined_tiles[3] = BLANK  # Topmost space is always BLANK.
    return combined_tiles


def make_move(board, move):
    """Carries out the move on the board.

    The move argument is either 'W', 'A', 'S', or 'D' and the function
    returns the resulting board data structure."""

    # The board is split up into four columns, which are different
    # depending on the direction of the move:
    if move == 'W':
        all_columns_spaces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                              [(1, 0), (1, 1), (1, 2), (1, 3)],
                              [(2, 0), (2, 1), (2, 2), (2, 3)],
                              [(3, 0), (3, 1), (3, 2), (3, 3)]]
    elif move == 'A':
        all_columns_spaces = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                              [(0, 1), (1, 1), (2, 1), (3, 1)],
                              [(0, 2), (1, 2), (2, 2), (3, 2)],
                              [(0, 3), (1, 3), (2, 3), (3, 3)]]
    elif move == 'S':
        all_columns_spaces = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                              [(1, 3), (1, 2), (1, 1), (1, 0)],
                              [(2, 3), (2, 2), (2, 1), (2, 0)],
                              [(3, 3), (3, 2), (3, 1), (3, 0)]]
    elif move == 'D':
        all_columns_spaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                              [(3, 1), (2, 1), (1, 1), (0, 1)],
                              [(3, 2), (2, 2), (1, 2), (0, 2)],
                              [(3, 3), (2, 3), (1, 3), (0, 3)]]

    # The board data structure after making the move:
    board_after_move = {}
    for column_spaces in all_columns_spaces:  # Loop over all 4 columns.
        # Get the tiles of this column (The first tile is the "bottom"
        # of the column):
        first_tile_space = column_spaces[0]
        second_tile_space = column_spaces[1]
        third_tile_space = column_spaces[2]
        fourth_tile_space = column_spaces[3]

        first_tile = board[first_tile_space]
        second_tile = board[second_tile_space]
        third_tile = board[third_tile_space]
        fourth_tile = board[fourth_tile_space]

        # Form the column and combine the tiles in it:
        column = [first_tile, second_tile, third_tile, fourth_tile]
        combined_tiles_column = combine_tiles_in_column(column)

        # Set up the new board data structure with the combined tiles:
        board_after_move[first_tile_space] = combined_tiles_column[0]
        board_after_move[second_tile_space] = combined_tiles_column[1]
        board_after_move[third_tile_space] = combined_tiles_column[2]
        board_after_move[fourth_tile_space] = combined_tiles_column[3]

    return board_after_move


def ask_for_player_move():
    """Asks the player for the direction of their next move (or quit).

    Ensures they enter a valid move: either 'W', 'A', 'S' or 'D'."""
    print('Enter move: (WASD or Q to quit)')
    while True:  # Keep looping until they enter a valid move.
        move = input('> ').upper()
        if move == 'Q':
            # End the program:
            print('Thanks for playing!')
            sys.exit()

        # Either return the valid move or loop back and ask again:
        if move in ('W', 'A', 'S', 'D'):
            return move
        else:
            print('Enter one of "W", "A", "S", "D", or "Q".')


def add_two_to_board(board):
    """Adds a new 2 tile randomly to the board."""
    while True:
        random_space = (random.randint(0, 3), random.randint(0, 3))
        if board[random_space] == BLANK:
            board[random_space] = 2
            return  # Return after finding one non-blank tile.


def is_full(board):
    """Returns True if the board data structure has no blanks."""
    # Loop over every space on the board:
    for x in range(4):
        for y in range(4):
            # If a space is blank, return False:
            if board[(x, y)] == BLANK:
                return False
    return True  # No space is blank, so return True.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

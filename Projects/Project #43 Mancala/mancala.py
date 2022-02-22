"""Mancala, by Al Sweigart al@inventwithpython.com
The ancient seed-sowing game.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: large, board game, game, two-player"""

import sys

# A tuple of the player's pits:
PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')

# A dictionary whose keys are pits and values are the opposite pit:
OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D',
                'K': 'E', 'L': 'F'}

# A dictionary whose keys are pits and values are the next pit in order:
NEXT_PIT = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
            '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G',
            'G': '2', '2': 'A'}

# Every pit label, in counterclockwise order starting with A:
PIT_LABELS = 'ABCDEF1LKJIHG2'

# How many seeds are in each pit at the start of a new game:
STARTING_NUMBER_OF_SEEDS = 4  # (!) Try changing this to 1 or 10.


def main():
    print('''Mancala, by Al Sweigart al@inventwithpython.com
    
The ancient two-player seed-sowing game. Grab the seeds from a pit on
your side and place one in each following pit, going counterclockwise
and skipping your opponent's store. If your last seed lands in an empty
pit of yours, move the opposite pit's seeds into that pit. The
goal is to get the most seeds in your store on the side of the board.
If the last placed seed is in your store, you get a free turn.

The game ends when all of one player's pits are empty. The other player
claims the remaining seeds for their store, and the winner is the one
with the most seeds.

More info at https://en.wikipedia.org/wiki/Mancala
''')
    input('Press Enter to begin...')

    game_board = get_new_board()
    player_turn = '1'  # Player 1 goes first.

    while True:  # Run a player's turn.
        # "Clear" the screen by printing many newlines, so the old
        # board isn't visible anymore.
        print('\n' * 60)
        # Display board and get the player's move:
        display_board(game_board)
        player_move = ask_for_player_move(player_turn, game_board)

        # Carry out the player's move:
        player_turn = make_move(game_board, player_turn, player_move)

        # Check if the game ended and a player has won:
        winner = check_for_winner(game_board)
        if winner == '1' or winner == '2':
            display_board(game_board)  # Display the board one last time.
            print('Player ' + winner + ' has won!')
            sys.exit()
        elif winner == 'tie':
            display_board(game_board)  # Display the board one last time.
            print('There is a tie!')
            sys.exit()


def get_new_board():
    """Return a dictionary representing a Mancala board in the starting
    state: 4 seeds in each pit and 0 in the stores."""

    # Syntactic sugar - use a shorter variable name:
    s = STARTING_NUMBER_OF_SEEDS

    # Create the data structure for the board, with 0 seeds in the
    # stores and the starting number of seeds in the pits:
    return {'1': 0, '2': 0, 'A': s, 'B': s, 'C': s, 'D': s, 'E':s,
            'F': s, 'G': s, 'H': s, 'I': s, 'J': s, 'K': s, 'L': s}


def display_board(board):
    """Displays the game board as ASCII-art based on the board
    dictionary."""

    seed_amounts = []
    # This 'GHIJK21ABCDEF' string is the order of the pits left to
    # right and top to bottom:
    for pit in 'GHIJKL21ABCDEF':
        num_seeds_in_this_pit = str(board[pit]).rjust(2)
        seed_amounts.append(num_seeds_in_this_pit)

    print("""
+------+------+--<<<<<-Player 2----+------+------+------+
2      |G     |H     |I     |J     |K     |L     |      1
       |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
S      |      |      |      |      |      |      |      S
T  {}  +------+------+------+------+------+------+  {}  T
O      |A     |B     |C     |D     |E     |F     |      O
R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
E      |      |      |      |      |      |      |      E
+------+------+------+-Player 1->>>>>-----+------+------+

    """.format(*seed_amounts))


def ask_for_player_move(player_turn, board):
    """Asks the player which pit on their side of the board they
    select to sow seeds from. Returns the uppercase letter label of the
    selected pit as a string."""

    while True:  # Keep asking the player until they enter a valid move.
        # Ask the player to select a pit on their side:
        if player_turn == '1':
            print('Player 1, choose move: A-F (or QUIT)')
        elif player_turn == '2':
            print('Player 2, choose move: G-L (or QUIT)')
        response = input('> ').upper().strip()

        # Check if the player wants to quit:
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # Make sure it is a valid pit to select:
        if (player_turn == '1' and response not in PLAYER_1_PITS) or (
            player_turn == '2' and response not in PLAYER_2_PITS
        ):
            print('Please pick a letter on your side of the board.')
            continue  # Ask player again for their move.
        if board.get(response) == 0:
            print('Please pick a non-empty pit.')
            continue  # Ask player again for their move.
        return response


def make_move(board, player_turn, pit):
    """Modify the board data structure so that the player 1 or 2 in
    turn selected pit as their pit to sow seeds from. Returns either
    '1' or '2' for whose turn it is next."""

    seeds_to_sow = board[pit]  # Get number of seeds from selected pit.
    board[pit] = 0  # Empty out the selected pit.

    while seeds_to_sow > 0:  # Continue sowing until we have no more seeds.
        pit = NEXT_PIT[pit]  # Move on to the next pit.
        if (player_turn == '1' and pit == '2') or (
            player_turn == '2' and pit == '1'
        ):
            continue  # Skip opponent's store.
        board[pit] += 1
        seeds_to_sow -= 1

    # If the last seed went into the player's store, they go again.
    if (pit == player_turn == '1') or (pit == player_turn == '2'):
        # The last seed landed in the player's store; take another turn.
        return player_turn

    # Check if last seed was in an empty pit; take opposite pit's seeds.
    if player_turn == '1' and pit in PLAYER_1_PITS and board[pit] == 1:
        opposite_pit = OPPOSITE_PIT[pit]
        board['1'] += board[opposite_pit]
        board[opposite_pit] = 0
    elif player_turn == '2' and pit in PLAYER_2_PITS and board[pit] == 1:
        opposite_pit = OPPOSITE_PIT[pit]
        board['2'] += board[opposite_pit]
        board[opposite_pit] = 0

    # Return the other player as the next player:
    if player_turn == '1':
        return '2'
    elif player_turn == '2':
        return '1'


def check_for_winner(board):
    """Looks at board and returns either '1' or '2' if there is a
    winner or 'tie' or 'no winner' if there isn't. The game ends when a
    player's pits are all empty; the other player claims the remaining
    seeds for their store. The winner is whoever has the most seeds."""

    player1_total = board['A'] + board['B'] + board['C']
    player1_total += board['D'] + board['E'] + board['F']
    player2_total = board['G'] + board['H'] + board['I']
    player2_total += board['J'] + board['K'] + board['L']

    if player1_total == 0:
        # Player 2 gets all the remaining seeds on their side:
        board['2'] += player2_total
        for pit in PLAYER_2_PITS:
            board[pit] = 0  # Set all pits to 0.
    elif player2_total == 0:
        # Player 1 gets all the remaining seeds on their side:
        board['1'] += player1_total
        for pit in PLAYER_1_PITS:
            board[pit] = 0  # Set all pits to 0.
    else:
        return 'no winner'  # No one has won yet.

    # Game is over, find player with largest score.
    if board['1'] > board['2']:
        return '1'
    elif board['2'] > board['1']:
        return '2'
    else:
        return 'tie'


# If program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()

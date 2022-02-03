"""Langton's Ant, by Al Sweigart al@inventwithpython.com
A cellular automata animation. Press Ctrl-C to stop.
More info: https://en.wikipedia.org/wiki/Langton%27s_ant
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, bext, simulation"""

import copy, random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the bext instructions at')
    print('https://pypi.org/project/Bext')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1
HEIGHT -= 1  # Adjustment for the quit message at the bottom.

NUMBER_OF_ANTS = 10  # TODO: Try changing this to 1 or 50.
PAUSE_AMOUNT = 0.1  # TODO: Try changing this to 1.0 or 0.0.

# TODO: Try changing these to make the ants look different:
ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

# TODO: Try changing these colors to one of 'black', 'red', 'green',
# 'yellow', 'blue', 'purple', 'cyan', or 'white'. (These are only
# colors that the bext module supports.
ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'


def main():
    bext.fg(ANT_COLOR)  # The ant's color is the foreground color.
    bext.bg(WHITE_TILE)  # Set the background to white to start.
    bext.clear()

    # Create a new board data structure:
    board = {'width': WIDTH, 'height': HEIGHT}

    # Create ant data structures:
    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
            'x': random.randint(0, WIDTH - 1),
            'y': random.randint(0, HEIGHT - 1),
            'direction': random.choice([NORTH, SOUTH, EAST, WEST]),
        }
        ants.append(ant)

    # Keep track of which tiles have changed and need to be redrawn on
    # the screen:
    changed_tiles = []
    i = 1

    while True:  # Main program loop.
        display_board(board, ants, changed_tiles, i)
        changed_tiles = []

        # next_board is what the board will look like on the next step in
        # the simulation. Start with a copy of the current step's board:
        next_board = copy.copy(board)

        # Run a single simulation step for each ant:
        for ant in ants:
            if board.get((ant['x'], ant['y']), False) == True:
                next_board[(ant['x'], ant['y'])] = False
                # Turn clockwise:
                if ant['direction'] == NORTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = NORTH
            else:
                next_board[(ant['x'], ant['y'])] = True
                # Turn counter clockwise:
                if ant['direction'] == NORTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = NORTH
            changed_tiles.append((ant['x'], ant['y']))

            # Move the ant forward in whatever direction it's facing:
            if ant['direction'] == NORTH:
                ant['y'] -= 1
            elif ant['direction'] == SOUTH:
                ant['y'] += 1
            elif ant['direction'] == WEST:
                ant['x'] -= 1
            elif ant['direction'] == EAST:
                ant['x'] += 1

            # If the ant goes past the edge of the screen,
            # it should wrap around to the other side.
            ant['x'] = ant['x'] % WIDTH
            ant['y'] = ant['y'] % HEIGHT

            changed_tiles.append((ant['x'], ant['y']))

        board = next_board
        i += 1


def display_board(board, ants, changed_tiles, i=1):
    """Displays the board and ants on the screen. The changed_tiles
    argument is a list of (x, y) tuples for tiles on the screen that
    have changed and need to be redrawn."""

    # Draw the board data structure:
    for x, y in changed_tiles:
        bext.goto(x, y)
        if board.get((x, y), False):
            bext.bg(BLACK_TILE)
        else:
            bext.bg(WHITE_TILE)

        ant_is_here = False
        for ant in ants:
            if (x, y) == (ant['x'], ant['y']):
                ant_is_here = True
                if ant['direction'] == NORTH:
                    print(ANT_UP, end='')
                elif ant['direction'] == SOUTH:
                    print(ANT_DOWN, end='')
                elif ant['direction'] == EAST:
                    print(ANT_LEFT, end='')
                elif ant['direction'] == WEST:
                    print(ANT_RIGHT, end='')
                break
        if not ant_is_here:
            print(' ', end='')

    # Display the quit message at the bottom of the screen:
    bext.goto(0, HEIGHT)
    bext.bg(WHITE_TILE)
    print(f'Press Ctrl-C to quit.    i = {i}', end='')

    sys.stdout.flush()  # Required for bext-using programs.
    time.sleep(PAUSE_AMOUNT)


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Langton\'s Ant, by Al Sweigart al@inventwithpython.com')
        sys.exit()  # When Ctrl-C is pressed, end the program.

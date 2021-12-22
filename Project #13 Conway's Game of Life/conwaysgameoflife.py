"""Conway's Game of Life, by Al Sweigart al@inventwithpython.com
The classical cellular automata simulation. Press Ctrl+C to stop.
More info at: https:en.wikipedia.org/wiki/Conway%27s_Game_of_Life
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, simulation"""

import copy, random, sys, time

# Set up the constants:
WIDTH = 79   # The width of the cell grid.
HEIGHT = 20  # The height of the cell grid.

# TODO: Try changing ALIVE to '#' or another character:
ALIVE = 'O'  # The character representing a living cell.
# TODO: Try changing DEAD to '.' or another character:
DEAD = ' '  # The character representing a dead cell.

# TODO: Try changing ALIVE to '|' and DEAD to '-'.

# The cells and next_cells are dictionaries for the state of the game.
# Their keys are (x, y) tuples and their values are one of the ALIVE
# or DEAD values.
next_cells = {}
# Put random dead and alive cells into next_cells:
for x in range(WIDTH):  # Loop over every possible columns.
    for y in range(HEIGHT):  # Loop over every possible row.
        # 50/50 chance for starting cells being alive or dead.
        if random.randint(0, 1) == 0:
            next_cells[(x, y)] = ALIVE  # Add a living cell.
        else:
            next_cells[(x, y)] = DEAD  # Add a dead cell.

while True:  # Main program loop.
    # Each iteration of this loop is a step of the simulation.

    print('\n' * 50)  # Separate each step with newlines.
    cells = copy.deepcopy(next_cells)

    # Print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')  # Print the # or space.
        print()  # Print a newline at the end of the row.
    print('Press Ctrl-C to quit.')

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighbouring coordinates of (x, y), even if they
            # wrap around the edge:
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the number of living neighbours:
            num_neighbours = 0
            if cells[(left, above)] == ALIVE:
                num_neighbours += 1  # Top-left neighbour is alive.
            if cells[(x, above)] == ALIVE:
                num_neighbours += 1  # Top neighbour is alive.
            if cells[(right, above)] == ALIVE:
                num_neighbours += 1  # Top-right neighbour is alive.
            if cells[(left, y)] == ALIVE:
                num_neighbours += 1  # Left neighbour is alive.
            if cells[(right, y)] == ALIVE:
                num_neighbours += 1  # Right neighbour is alive.
            if cells[(left, below)] == ALIVE:
                num_neighbours += 1  # Bottom-left neighbour is alive.
            if cells[(x, below)] == ALIVE:
                num_neighbours += 1  # Bottom neighbour is alive.
            if cells[(right, below)] == ALIVE:
                num_neighbours += 1  # Bottom-right neighbour is alive.

            # Set cell based on Conway's Game of Life rules:
            if cells[(x, y)] == ALIVE and (num_neighbours == 2
                                           or num_neighbours == 3):
                # Living cells with 2 or 3 num_neighbours stay alive:
                next_cells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and num_neighbours == 3:
                # Dead cells with 3 neighbours become alive:
                next_cells[(x, y)] = ALIVE
            else:
                # Everything else dies or stays dead:
                next_cells[(x, y)] = DEAD

    try:
        time.sleep(1)  # Add a 1 second pause to reduce flickering.
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print('By Al Sweigart al@inventwithpython.com')
        sys.exit()  # When Ctrl-C is pressed, end the program.

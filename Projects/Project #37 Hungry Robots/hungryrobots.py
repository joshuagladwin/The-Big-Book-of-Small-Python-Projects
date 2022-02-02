"""Hungry Robots, by Al Sweigart al@inventwithpython.com
Escape the hungry robots by making them crash into each other.
View the original code at https://nostarch.com/big-book-small-python-projects.
Tags: large, game"""

import random, sys

# Set up the constants:
WIDTH = 40          # TODO: Try changing this to 70 or 10.
HEIGHT = 20         # TODO: Try changing this to 10.
NUM_ROBOTS = 10     # TODO: Try changing this to 1 or 30.
NUM_TELEPORT = 2    # TODO: Try changing this to 0 or 9999.
NUM_DEAD_ROBOTS = 2  # TODO: Try changing this to 0 or 20.
NUM_WALLS = 100      # TODO: Try changing this 0 or 1000.

EMPTY_SPACE = ' '   # TODO: Try changing this to '.'.
PLAYER = '@'        # TODO: Try changing this to 'R'.
ROBOT = 'R'         # TODO: Try changing this to '@'.
DEAD_ROBOT = 'X'    # TODO: Try changing this to 'R'.

# TODO: Try changing this to '#' or 'O' or ' ':
WALL = chr(9617)  # Character 9617 is '░'


def main():
    print(f'''Hungry Robots, be Al Sweigart al@inventwithpython.com
    
You are trapped in a maze with hungry robots! You don't know why robots
need to eat, but you don't want to find out. The robots are badly
programmed and will move directly toward you, even if blocked by walls.
You must trick the robots into crashing into each other (or dead robots)
without being caught. You have a personal teleporter device, but it only
has enough battery for {NUM_TELEPORT} trips. Keep in mind, you and robots 
can slip through the corners of two diagonal walls!
''')

    input('Press Enter to begin...')

    # Set up a new game:
    board = get_new_board()
    robots = add_robots(board)
    player_position = get_random_empty_space(board, robots)
    while True:  # Main game loop.
        display_board(board, robots, player_position)

        if len(robots) == 0:  # Check if the player has won.
            print('All the robots have crashed into each other and you')
            print('lived to tell the tale! Good job!')
            sys.exit()

        # Move the player and robots:
        player_position = ask_for_player_move(board, robots, player_position)
        robots = move_robots(board, robots, player_position)

        for x, y in robots:  # Check if the player has lost.
            if (x, y) == player_position:
                display_board(board, robots, player_position)
                print('You have been caught by a robot!')
                sys.exit()


def get_new_board():
    """Returns a dictionary that represents the baord. The keys are
    (x, y) tuples of integer indexes for board positions, the values are
    WALL, EMPTY_SPACE, or DEAD_ROBOT. The dictionary also has the key
    'teleports' for the number of teleports the player has left.
    The living robots are stored separately form the board dictionary."""
    board = {'teleports': NUM_TELEPORT}

    # Create an empty board:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    # Add walls on the edges of the board:
    for x in range(WIDTH):
        board[(x, 0)] = WALL  # Make top wall.
        board[(x, HEIGHT - 1)] = WALL  # Make bottom wall.
    for y in range(HEIGHT):
        board[(0, y)] = WALL  # Make left wall.
        board[(WIDTH - 1, y)] = WALL  # Make right wall.

    # Add the random walls:
    for i in range(NUM_WALLS):
        x, y = get_random_empty_space(board, [])
        board[(x, y)] = WALL

    # Add the starting dead robots:
    for i in range(NUM_DEAD_ROBOTS):
        x, y = get_random_empty_space(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def get_random_empty_space(board, robots):
    """Return a (x, y) integer tuple of an empty space on the board."""
    while True:
        random_x = random.randint(1, WIDTH - 2)
        random_y = random.randint(1, HEIGHT - 2)
        if is_empty(random_x, random_y, board, robots):
            break
    return (random_x, random_y)


def is_empty(x, y, board, robots):
    """Return True if the (x, y) is empty on the board and there's also
    no robot there."""
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots


def add_robots(board):
    """Add NUM_ROBOTS number of robots to empty spaces on the board and
    return a list of these (x, y) spaces where robots are now located."""
    robots = []
    for i in range(NUM_ROBOTS):
        x, y = get_random_empty_space(board, robots)
        robots.append((x, y))
    return robots


def display_board(board, robots, player_position):
    """Display the board, robots, and player on the screen."""
    # Loop over every space on the board:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Draw the appropriate character:
            if board[(x, y)] == WALL:
                print(WALL, end='')
            elif board[(x, y)] == DEAD_ROBOT:
                print(DEAD_ROBOT, end='')
            elif (x, y) == player_position:
                print(PLAYER, end='')
            elif (x, y) in robots:
                print(ROBOT, end='')
            else:
                print(EMPTY_SPACE, end='')
        print()  # Print a newline.


def ask_for_player_move(board, robots, player_position):
    """Returns the (x, y) integer tuple of the place the player moves
    next, given their current location and the walls of the board."""
    player_x, player_y = player_position

    # Find which directions aren't blocked by a wall:
    q = 'Q' if is_empty(player_x - 1, player_y - 1, board, robots) else ' '
    w = 'W' if is_empty(player_x + 0, player_y - 1, board, robots) else ' '
    e = 'E' if is_empty(player_x + 1, player_y - 1, board, robots) else ' '
    d = 'D' if is_empty(player_x + 1, player_y + 0, board, robots) else ' '
    c = 'C' if is_empty(player_x + 1, player_y + 1, board, robots) else ' '
    x = 'X' if is_empty(player_x + 0, player_y + 1, board, robots) else ' '
    z = 'Z' if is_empty(player_x - 1, player_y + 1, board, robots) else ' '
    a = 'A' if is_empty(player_x - 1, player_y + 0, board, robots) else ' '
    all_moves = (q + w + e + d + c + x + a + z + 'S')

    while True:
        # Get the player's move:
        print(f'(T)eleports remaining: {board["teleports"]}')
        print(f'                    ({q}) ({w}) ({e})')
        print(f'                    ({a}) (S) ({d})')
        print(f'Enter move or QUIT: ({z}) ({x}) ({c})')

        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'T' and board["teleports"] > 0:
            # Teleport the player to a random empty space:
            board['teleports'] -= 1
            return get_random_empty_space(board, robots)
        elif move != '' and move in all_moves:
            # Return the new player position based on their move:
            return {'Q': (player_x - 1, player_y - 1),
                    'W': (player_x + 0, player_y - 1),
                    'E': (player_x + 1, player_y - 1),
                    'D': (player_x + 1, player_y + 0),
                    'C': (player_x + 1, player_y + 1),
                    'X': (player_x + 0, player_y + 1),
                    'Z': (player_x - 1, player_y + 1),
                    'A': (player_x - 1, player_y + 0),
                    'S': (player_x, player_y)}[move]


def move_robots(board, robot_positions, player_position):
    """Return a list of (x, y) tuples of new robot positions after they
    have tried to move toward the player."""
    player_x, player_y = player_position
    next_robots_positions = []

    while len(robot_positions) > 0:
        robot_x, robot_y = robot_positions[0]

        # Determine the direction the robot moves.
        if robot_x < player_x:
            move_x = 1  # Move right.
        elif robot_x > player_x:
            move_x = -1  # Move left.
        elif robot_x == player_x:
            move_x = 0  # Don't move horizontally.

        if robot_y < player_y:
            move_y = 1  # Move up.
        elif robot_y > player_y:
            move_y = -1  # Move down.
        elif robot_y == player_y:
            move_y = 0  # Don't move vertically.

        # Check if the robot would run into a wall, and adjust course:
        if board[(robot_x + move_x, robot_y + move_y)] == WALL:
            # Robot would run into a wall, so come up with a new move:
            if board[(robot_x + move_x, robot_y)] == EMPTY_SPACE:
                move_y = 0  # Robot can't move horizontally.
            elif board[(robot_x, robot_y + move_y)] == EMPTY_SPACE:
                move_x = 0  # Robot can't move vertically.
            else:
                # Robot can't move.
                move_x = 0
                move_y = 0
        new_robot_x = robot_x + move_x
        new_robot_y = robot_y + move_y

        if (board[(robot_x, robot_y)] == DEAD_ROBOT
            or board[(new_robot_x, new_robot_y)] == DEAD_ROBOT):
            # Robot is at crash site, remove it.
            del robot_positions[0]
            continue

        # Check if it moves into a robot, the destroy both robots:
        if (new_robot_x, new_robot_y) in next_robots_positions:
            board[(new_robot_x, new_robot_y)] = DEAD_ROBOT
            next_robots_positions.remove((new_robot_x, new_robot_y))
        else:
            next_robots_positions.append((new_robot_x, new_robot_y))

        # Remove robots from robot_positions as they move/
        del robot_positions[0]
    return next_robots_positions


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()

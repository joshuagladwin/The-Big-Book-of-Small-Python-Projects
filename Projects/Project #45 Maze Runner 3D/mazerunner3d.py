"""Maze Runner 3D, by Al Sweigart al@inventwithpython.com
Move around a maze and try to escape... in 3D!
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: extra-large, artistic, game, maze"""

import copy, sys, os

# Set up the constants:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)  # Character 9617 is '░'
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'


def wall_str_to_wall_dict(wall_str):
    """Takes a string representation of a wall drawing, (like those in
    ALL_OPEN or CLOSED) and returns a representation in a dictionary
    with (x, y) tuples as keys and single-character strings of the
    character to draw at that x, y location."""
    wall_dict = {}
    height = 0
    width = 0
    for y, line in enumerate(wall_str.splitlines()):
        if y > height:
            height = y
        for x, character in enumerate(line):
            if x > width:
                width = x
            wall_dict[(x, y)] = character
    wall_dict['height'] = height + 1
    wall_dict['width'] = width + 1
    return wall_dict

EXIT_DICT = {(0, 0): 'E', (1, 0): 'X', (2, 0): 'I',
             (3, 0): 'T', 'height': 1, 'width': 4}

# The way we create the strings to display is by converting the pictures
# in these multiline strings to dictionaries using wallStrToWallDict().
# Then we compose the wall for the player's location and direction by
# "pasting" the wall dictionaries in CLOSED on top of the wall dictionary
# in ALL_OPEN.

ALL_OPEN = wall_str_to_wall_dict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................'''.strip())
# The strip() call is used to remove the newline
# at the start of this multiline string.

CLOSED = {}
CLOSED['A'] = wall_str_to_wall_dict(r'''
_____
.....
.....
.....
_____'''.strip())  # Paste to 6, 4

CLOSED['B'] = wall_str_to_wall_dict(r'''
.\.
..\
...
...
...
../
./.'''.strip())  # Paste to 4, 3.

CLOSED['C'] = wall_str_to_wall_dict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________'''.strip())  # Paste to 3, 1.

CLOSED['D'] = wall_str_to_wall_dict(r'''
./.
/..
...
...
...
\..
.\.'''.strip())  # Paste to 10, 3.

CLOSED['E'] = wall_str_to_wall_dict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..'''.strip())  # Paste to 0, 0.

CLOSED['F'] = wall_str_to_wall_dict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..'''.strip())  # Paste to 12, 0.

def display_wall_dict(wall_dict):
    """Display a wall dictionary, as returned by wall_str_to_wall_dict(), on
    the screen."""
    print(BLOCK * (wall_dict['width'] + 2))
    for y in range(wall_dict['height']):
        print(BLOCK, end='')
        for x in range(wall_dict['width']):
            wall = wall_dict[(x, y)]
            if wall == '.':
                wall = ' '
            print(wall, end='')
        print(BLOCK)  # Print block with a newline.
    print(BLOCK * (wall_dict['width'] + 2))


def paste_wall_dict(src_wall_dict, dst_wall_dict, left, top):
    """Copy the wall representation dictionary in src_wall_dict on top of
    the one in dst_wall_dict, offset to the positions given by left, top."""
    dst_wall_dict = copy.copy(dst_wall_dict)
    for x in range(src_wall_dict['width']):
        for y in range(src_wall_dict['height']):
            dst_wall_dict[(x + left, y + top)] = src_wall_dict[(x, y)]
    return dst_wall_dict


def make_wall_dict(maze, player_x, player_y, player_direction, exit_x, exit_y):
    """From the player's position and direction in the maze (which has
    an exit at exit_x, exit_y), create the wall representation dictionary
    by pasting wall dictionaries on top of ALL_OPEN, then return it."""

    # The A-F "sections" (which are relative to the player's direction)
    # determine which walls in the maze we check to see if we need to
    # paste them over the wall representation dictionary we're creating.

    if player_direction == NORTH:
        # Map of the sections, relative  A
        # to the player @:              BCD (Player facing north)
        #                               E@F
        offsets = (('A', 0, -2), ('B', -1, -1), ('C', 0, -1),
                   ('D', 1, -1), ('E', -1, 0), ('F', 1, 0))
    if player_direction == SOUTH:
        # Map of the sections, relative F@E
        # to the player @:              DCB (Player facing south)
        #                                A
        offsets = (('A', 0, 2), ('B', 1, 1), ('C', 0, 1),
                   ('D', -1, 1), ('E', 1, 0), ('F', -1, 0))
    if player_direction == EAST:
        # Map of the sections, relative EB
        # to the player @:              @CA (Player facing east)
        #                               FD
        offsets = (('A', 2, 0), ('B', 1, -1), ('C', 1, 0),
                   ('D', 1, 1), ('E', 0, -1), ('F', 0, 1))
    if player_direction == WEST:
        # Map of the sections, relative  DF
        # to the player @:              AC@ (Player facing west)
        #                                BE
        offsets = (('A', -2, 0), ('B', -1, 1), ('C', -1, 0),
                   ('D', -1, -1), ('E', 0, 1), ('F', 0, -1))

    section = {}
    for sec, x_off, y_off in offsets:
        section[sec] = maze.get((player_x + x_off, player_y + y_off), WALL)
        if (player_x + x_off, player_y + y_off) == (exit_x, exit_y):
            section[sec] = EXIT

    wall_dict = copy.copy(ALL_OPEN)
    PASTE_CLOSED_TO = {'A': (6, 4), 'B': (4, 3), 'C': (3, 1),
                       'D': (10, 3), 'E': (0, 0), 'F': (12, 0)}
    for sec in 'ABDCEF':
        if section[sec] == WALL:
            wall_dict = paste_wall_dict(CLOSED[sec], wall_dict,
                PASTE_CLOSED_TO[sec][0], PASTE_CLOSED_TO[sec][1])

    # Draw the EXIT sign if needed:
    if section['C'] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 7, 9)
    if section['E'] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 0, 11)
    if section['F'] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 13, 11)

    return wall_dict


print('Maze Runner 3D, by Al Sweigart al@inventwithpython.com')
print('(Maze files are generated by mazemakerrec.py)')

# Get the maze file's filename from the user:
os.chdir('maze_files')
while True:
    print('Enter the filename of the maze (or LIST or QUIT):')
    filename = input('> ')

    # List all the maze files in the current folder:
    if filename.upper() == 'LIST':
        print('Maze files found in', os.getcwd())
        for file_in_current_folder in os.listdir():
            if (file_in_current_folder.startswith('maze')
            and file_in_current_folder.endswith('.txt')):
                print('  ', file_in_current_folder)
        continue

    if filename.upper() == 'QUIT':
        sys.exit()

    if os.path.exists(filename):
        break
    print('There is no file named', filename)

# Load the maze from a file:
maze_file = open(filename)
maze = {}
lines = maze_file.readlines()
p_x = None
p_y = None
exit_x = None
exit_y = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT), f'Invalid character \
        at column {x + 1}, line {y + 1}'
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            p_x, p_y = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exit_x, exit_y = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert p_x != None and p_y != None, 'No start point in file.'
assert exit_x != None and exit_y != None, 'No point exit in file.'
p_dir = NORTH


while True:  # Main game loop.
    display_wall_dict(make_wall_dict(maze, p_x, p_y, p_dir, exit_x, exit_y))

    while True:  # Get user move.
        print(f'Location({p_x}, {p_y})  Direction: {p_dir}')
        print('                   (W)')
        print('Enter direction: (A) (D)  or QUIT.')
        move = input('> ').upper()

        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if (move not in ['F', 'L', 'R', 'W', 'A', 'D']
            and not move.startswith('T')):
            print('Please enter one of F, L, or R (or W, A, D).')
            continue

        # Move the player according to their intended move:
        if move == 'F' or move == 'W':
            if p_dir == NORTH and maze[(p_x, p_y - 1)] == EMPTY:
                p_y -= 1
                break
            if p_dir == SOUTH and maze[(p_x, p_y + 1)] == EMPTY:
                p_y += 1
                break
            if p_dir == EAST and maze[(p_x + 1, p_y)] == EMPTY:
                p_x += 1
                break
            if p_dir == WEST and maze[(p_x - 1, p_y)] == EMPTY:
                p_x -= 1
                break
        elif move == 'L' or move == 'A':
            p_dir = {NORTH: WEST, WEST: SOUTH,
                     SOUTH: EAST, EAST: NORTH}[p_dir]
            break
        elif move == 'R' or move == 'D':
            p_dir = {NORTH: EAST, EAST: SOUTH,
                     SOUTH: WEST, WEST: NORTH}[p_dir]
            break
        elif move.startswith('T'):  # Cheat code: 'T x,y'
            p_x, p_y = move.split()[1].split(',')
            p_x = int(p_x)
            p_y = int(p_y)
            break
        else:
            print('You cannot move in that direction.')

    if (p_x, p_y) == (exit_x, exit_y):
        print('You have reached the exit! Good job!')
        print('Thanks for playing!')
        sys.exit()
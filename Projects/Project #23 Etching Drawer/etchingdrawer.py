"""Etching Drawer, by Al Sweigart al@inventwithpython.com
An art program that draws a continuous line around the screen using the
WASD keys. Inspired by Etch A Sketch toys.

For example, you can draw Hilbert Curve fractal with:
SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

Or an even larger Hilbert Curve fractal with:
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
AAAAWAASSDDSAASSDDWDDSDDWWAAWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWA
AWDDDDSDDWWAAWDDWWAASAAWAASSDDSAAAAWAASAAAAWDDWAAWDDDDSDDWWWAASAAAAWD
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD

View the original code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic"""

import shutil, sys

# Set up the constants for line characters:
UP_DOWN_CHAR = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR = chr(9472)  # Character 9472 is '─'
DOWN_RIGHT_CHAR = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR = chr(9488)  # Character 9488 is '┐'
UP_RIGHT_CHAR = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR = chr(9496)  # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR = chr(9500)  # Character 9500 is '├'
UP_DOWN_LEFT_CHAR = chr(9508)  # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR = chr(9524)  # Character 9524 is '┴'
CROSS_CHAR = chr(9532)  # Character 9532 is '┼'
# A list of chr() codes is at https://inventwithpython.com/chr

# Get the size of the terminal window:
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
CANVAS_WIDTH -= 1
# Leave room at the bottom few rows for the command info lines.
CANVAS_HEIGHT -= 5

"""The keys for canvas will be (x, y) integer tuples for the coordinate,
and teh value is a set of letters W, A, S, D that tell what kind of line
 should be drawn."""
canvas = {}
cursor_x = 0
cursor_y = 0


def get_canvas_string(canvas_data, cx, cy):
    """Returns a multiline string of the line drawn in canvas_data."""
    canvas_str = ''

    """canvas_data is a dictionary with (x, y) tuple keys and values that
    are sets of 'W', 'A', 'S', and /or 'D' strings to show which
    directions the lines are drawn at each xy point."""
    for row_num in range(CANVAS_HEIGHT):
        for column_num in range(CANVAS_WIDTH):
            if column_num == cx and row_num == cy:
                canvas_str += '#'
                continue

            # Add the line character for this point to canvasStr.
            cell = canvas_data.get((column_num, row_num))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvas_str += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvas_str += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvas_str += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvas_str += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvas_str += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvas_str += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvas_str += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvas_str += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvas_str += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvas_str += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvas_str += CROSS_CHAR
            elif cell == None:
                canvas_str += ' '
        canvas_str += '\n'  # Add a newline at the end of each row.
    return canvas_str


moves = []
while True:  # Main program loop.
    # Draw the liens based on the data in canvas:
    print(get_canvas_string(canvas, cursor_x, cursor_y))

    print('WASD keys to move, H for help, C to clear, '
          'R to clear and reset to start, F to save, or QUIT.')
    response = input('> ').upper()

    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()  # Quit the program.
    elif response == 'H':
        print('Enter W, A, S, and D characters to move the cursor and')
        print('draw a line behind it as it moves. For example, ddd')
        print('draws a line going right and sssdddwwwaaa draws a bos.')
        print()
        print('You can save your drawing to a text file by entering F.')
        input('Press Enter to return to the program...')
        continue
    elif response == 'C':
        canvas = {}  # Erase the canvas data.
        moves.append('C')  # Record this move.
    elif response == 'R':
        canvas = {}  # Erase the canvas data.
        cursor_x, cursor_y = 0, 0  # Reset the cursor to (0,0)
        moves.append('R')  # Record this move.
    elif response == 'F':
        # Save the canvas string to a text file:
        try:
            print('Enter filename to save to:')
            filename = input('> ')

            # Make sure the filename ends with .txt:
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(get_canvas_string(canvas, None, None))
        except:
            print('ERROR: Could not save file.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue  # Ignore this letter and continue to the next one.
        moves.append(command)  # Record this move.

        # The first line we add needs to form a full line:
        if canvas == {}:
            if command in ('W', 'S'):
                # Make the first line a horizontal one:
                canvas[(cursor_x, cursor_y)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                # Make the first line a vertical one:
                canvas[(cursor_x, cursor_y)] = set(['A', 'D'])

        # Update x and y:
        if command == 'W' and cursor_y > 0:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_y = cursor_y - 1
        elif command == 'S' and cursor_y < CANVAS_HEIGHT - 1:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_y = cursor_y + 1
        elif command == 'A' and cursor_x > 0:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_x = cursor_x - 1
        elif command == 'D' and cursor_x < CANVAS_WIDTH - 1:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_x = cursor_x + 1
        else:
            # If the cursor doesn't move because it would have moved off
            # the edge of the canvas, then don't change the set at
            # canvas[(cursor_x, cursor_y)].
            continue

        # If there's no set for (cursor_x, cursor_y), add an empty set:
        if (cursor_x, cursor_y) not in canvas:
            canvas[(cursor_x, cursor_y)] = set()

        # Add the direction string to this xy point's set:
        if command == 'W':
            canvas[(cursor_x, cursor_y)].add('S')
        elif command == 'S':
            canvas[(cursor_x, cursor_y)].add('W')
        elif command == 'A':
            canvas[(cursor_x, cursor_y)].add('D')
        elif command == 'D':
            canvas[(cursor_x, cursor_y)].add('A')

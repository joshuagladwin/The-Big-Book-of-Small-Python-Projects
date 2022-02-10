"""Mondrian Art Generator, by Al Sweigart al@inventwithpython.com
Randomly generates art in the style of Piet Mondrian.
More info at: https://en.wikipedia.org/wiki/Piet_Mondrian
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, bext"""

import sys, random

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
MIN_X_INCREASE = 6
MAX_X_INCREASE = 16
MIN_Y_INCREASE = 3
MAX_Y_INCREASE = 6
WHITE = 'white'
BLACK = 'black'
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'

# Setup the screen:
width, height = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
width -= 1

height -= 3

while True:  # Main application loop.
    # Pre-populate the canvas with blank spaces:
    canvas = {}
    for x in range(width):
        for y in range(height):
            canvas[(x, y)] = WHITE

    # Generate vertical lines:
    number_of_segments_to_delete = 0
    x = random.randint(MIN_X_INCREASE, MAX_X_INCREASE)
    while x < width - MIN_X_INCREASE:
        number_of_segments_to_delete += 1
        for y in range(height):
            canvas[(x, y)] = BLACK
        x += random.randint(MIN_X_INCREASE, MAX_X_INCREASE)

    # Generate horizontal lines:
    y = random.randint(MIN_Y_INCREASE, MAX_X_INCREASE)
    while y < height - MIN_Y_INCREASE:
        number_of_segments_to_delete += 1
        for x in range(width):
            canvas[(x, y)] = BLACK
        y += random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)

    number_of_rectangles_to_paint = number_of_segments_to_delete - 3
    number_of_segments_to_delete = int(number_of_segments_to_delete * 1.5)

    # Randomly select points and try to remove them:
    for i in range(number_of_segments_to_delete):
        while True:  # Keep selecting segments to try to delete.
            # Get a random start point on an existing segment:
            start_x = random.randint(1, width - 2)
            start_y = random.randint(1, height - 2)
            if canvas[(start_x, start_y)] == WHITE:
                continue

            # Find out if we're on a vertical or horizontal segment:
            if (canvas[(start_x - 1, start_y)] == WHITE and
                canvas[(start_x + 1, start_y)] == WHITE):
                orientation = 'vertical'
            elif (canvas[(start_x, start_y - 1)] == WHITE and
                  canvas[(start_x, start_y + 1)] == WHITE):
                orientation = 'horizontal'
            else:
                # The start point is on an intersection,
                # so get a new random start point:
                continue

            points_to_delete = [(start_x, start_y)]

            can_delete_segment = True
            if orientation == 'vertical':
                # Go up one path from the start point, and
                # see if we can remove this segment:
                for change_y in (-1, 1):
                    y = start_y
                    while 0 < y < height - 1:
                        y += change_y
                        if (canvas[(start_x - 1, y)] == BLACK and
                            canvas[(start_x + 1, y)] == BLACK):
                            # We've found a four-way intersection.
                            break
                        elif (canvas[(start_x - 1, y)] == WHITE and
                              canvas[(start_x + 1, y)] == BLACK) or \
                             (canvas[(start_x - 1, y)] == BLACK and
                              canvas[(start_x + 1, y)] == WHITE):
                            # We've found a T-intersection; we can't
                            # delete this segment:
                            can_delete_segment = False
                            break
                        else:
                            points_to_delete.append((start_x, y))

            elif orientation == 'horizontal':
                # Go up one path from the start point, and
                # see if we can remove this segment:
                for change_x in (-1, 1):
                    x = start_x
                    while 0 < x < width - 1:
                        x += change_x
                        if (canvas[(x, start_y - 1)] == BLACK and
                            canvas[(x, start_y + 1)] == BLACK):
                            # We've found a four-way intersection.
                            break
                        elif (canvas[(x, start_y - 1)] == WHITE and
                              canvas[(x, start_y + 1)] == BLACK) or \
                             (canvas[(x, start_y - 1)] == BLACK and
                              canvas[(x, start_y + 1)] == WHITE):
                            # We've found a T-intersection; we can't
                            # delete this segment:
                            can_delete_segment = False
                            break
                        else:
                            points_to_delete.append((x, start_y))
            if not can_delete_segment:
                continue  # Get a new random start point.
            break  # Move on to delete the segment.

        # If we can delete this segment, set all the points to white:
        for x, y in points_to_delete:
            canvas[(x, y)] = WHITE

    # Add the border lines:
    for x in range(width):
        canvas[(x, 0)] = BLACK  # Top border.
        canvas[(x, height - 1)] = BLACK  # Bottom border.
    for y in range(height):
        canvas[(0, y)] = BLACK # Left border.
        canvas[(width - 1, y)] = BLACK  # Right border.

    # Paint the rectangles@
    for i in range(number_of_rectangles_to_paint):
        while True:
            start_x = random.randint(1, width - 2)
            start_y = random.randint(1, height - 2)

            if canvas[(start_x, start_y)] != WHITE:
                continue  # Get a new random start point.
            else:
                break

        # Flood fill algorithm:
        color_to_paint = random.choice([RED, YELLOW, BLUE, BLACK])
        points_to_paint = set([(start_x, start_y)])
        while len(points_to_paint) > 0:
            x, y = points_to_paint.pop()
            canvas[(x, y)] = color_to_paint
            if canvas[(x - 1, y)] == WHITE:
                points_to_paint.add((x - 1, y))
            if canvas[(x + 1, y)] == WHITE:
                points_to_paint.add((x + 1, y))
            if canvas[(x, y - 1)] == WHITE:
                points_to_paint.add((x, y - 1))
            if canvas[(x, y + 1)] == WHITE:
                points_to_paint.add((x, y + 1))

    # Draw the canvas data structure:
    for y in range(height):
        for x in range(width):
            bext.bg(canvas[(x, y)])
            print(' ', end='')

        print()

    # Prompt user to create a new one:
    try:
        input('Press Enter for another work of art, of Ctrl-C to quit.')
    except:
        sys.exit()



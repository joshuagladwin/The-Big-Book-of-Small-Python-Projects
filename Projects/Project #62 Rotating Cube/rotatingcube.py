"""Rotating Cube, by Al Sweigart al@inventwithpython.com
A rotating cube animation. Press Ctrl-C to stop.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, math"""

# This program must be run in a Terminal/Command Prompt window.

import math, time, sys, os

# Set up the constants:
PAUSE_AMOUNT = 0.1  # Pause length of one-tenth of a second.
WIDTH, HEIGHT = 80, 24
SCALE_X = (WIDTH - 4) // 8
SCALE_Y = (HEIGHT - 4) // 8
# Text cells are twice as tall as they are wide, so set SCALE_Y:
SCALE_Y *= 2
TRANSLATE_X = (WIDTH - 4) // 2
TRANSLATE_Y = (HEIGHT - 4) // 2

# TODO: Try changing this to '#' or '*' or some other character:
LINE_CHAR = chr(9608)  # Character 9608 is '█'

# TODO: Try setting two of these values to zero to rotate the cube only
# along a single axis:
X_ROTATE_SPEED = 0.03
Y_ROTATE_SPEED = 0.08
Z_ROTATE_SPEED = 0.13

# This program stores XYZ coordinates in lists, with the X coordinate
# at index 0, Y at 1, and Z at 2. These constants make our code more
# readable when accessing the coordinates in these lists.
X = 0
Y = 1
Z = 2


def line(x1, y1, x2, y2):
    """Returns a list of points in a line between the given points.

    Uses the Bresenham line algorithm. More info at:
    https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""
    points = []  # Contains the points of the line.
    # "Steep" means the slope of the line is greater than 45 degrees or
    # less than -45 degrees:

    # Check for the special case where the start and end points are
    # certain neighbors, which this function doesn't handle correctly,
    # and return a hard coded list instead:
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]

    is_steep = abs(y2 - y1) > abs(x2 - x1)
    if is_steep:
        # This algorithm only handles non-steep lines, so let's change
        # the slope to non-steep and change it back later.
        x1, y1 = y1, x1  # Swap x1 and y1
        x2, y2 = y2, x2  # Swap x2 and y2
    is_reversed = x1 > x2  # True if the line goes right-to-left.

    if is_reversed:  # Get the points on the line going right-to-left.
        x1, x2 = x2, x1  # Swap x1 and x2
        y1, y2 = y2, y1  # Swap y1 and y2

        delta_x = x2 - x1
        delta_y = abs(y2 - y1)
        extra_y = int(delta_x / 2)
        current_y = y2
        if y1 < y2:
            y_direction = 1
        else:
            y_direction = -1
        # Calculate the y for every x in this line:
        for current_x in range(x2, x1 - 1, -1):
            if is_steep:
                points.append((current_y, current_x))
            else:
                points.append((current_x, current_y))
            extra_y -= delta_y
            if extra_y <= 0:  # Only change y once extra_y <= 0.
                current_y -= y_direction
                extra_y += delta_x
                
    else:  # Get the points on the line going left to right.
        delta_x = x2 - x1
        delta_y = abs(y2 - y1)
        extra_y = int(delta_x / 2)
        current_y = y1
        if y1 < y2:
            y_direction = 1
        else:
            y_direction = -1
        # Calculate the y for every x in this line:
        for current_x in range(x1, x2 + 1):
            if is_steep:
                points.append((current_y, current_x))
            else:
                points.append((current_x, current_y))
            extra_y -= delta_y
            if extra_y <= 0:  # Only change y once extra_y <= 0.
                current_y += y_direction
                extra_y += delta_x
    return points

def rotate_point(x, y, z, ax, ay, az):
    """Returns an (x, y, z) tuple of the x, y, z arguments rotated.
    
    The rotation happens around the 0, 0, 0 origin by angles
    ax, ay, az (in radians).
        Directions of each axis:
         -y
          |
          +-- +x
         / 
        +z
    """
    
    # Rotate around x axis:
    rotated_x = x
    rotated_y = (y * math.cos(ax)) - (z * math.sin(ax))
    rotated_z = (y * math.sin(ax)) + (z * math.cos(ax))
    x, y, z = rotated_x, rotated_y, rotated_z

    # Rotate around y axis:
    rotated_x = (z * math.sin(ay)) + (x * math.cos(ay))
    rotated_y = y
    rotated_z = (z * math.cos(ay)) - (x * math.sin(ay))
    x, y, z = rotated_x, rotated_y, rotated_z

    # Rotate around z axis:
    rotated_x = (x * math.cos(az)) - (y * math.sin(az))
    rotated_y = (x * math.sin(az)) + (y * math.cos(az))
    rotated_z = z

    return (rotated_x, rotated_y, rotated_z)


def adjust_point(point):
    """Adjusts the 3D XYZ point to a 2D XY point fit for displaying on
    the screen. This resizes this 2D point by a scale of SCALE_X and
    SCALE_Y, then moves the point by TRANSLATE_X and TRANSLATE_Y."""
    return (int(point[X] * SCALE_X + TRANSLATE_X),
            int(point[Y] * SCALE_Y + TRANSLATE_Y))


"""CUBE_CORNERS stores the XYZ coordinates of the corners of a cube.
The indexes for each corner in CUBE_CORNERS are marked in this diagram:
      0---1
     /|  /|
    2---3 |
    | 4-|-5
    |/  |/
    6---7"""
CUBE_CORNERS = [[-1, -1, -1],  # Point 0
                [ 1, -1, -1],  # Point 1
                [-1, -1,  1],  # Point 2
                [ 1, -1,  1],  # Point 3
                [-1,  1, -1],  # Point 4
                [ 1,  1, -1],  # Point 5
                [-1,  1,  1],  # Point 6
                [ 1,  1,  1]]  # Point 7
# rotated_corners stores the XYZ coordinates from CUBE_CORNERS after
# they've been rotated by rx, ry, and rz amounts:
rotated_corners = [None, None, None, None, None, None, None, None]
# Rotation amounts for each axis:
x_rotation = 0.0
y_rotation = 0.0
z_rotation = 0.0

try:
    while True:  # Main program loop.
        # Rotate the cube along different axes by different amounts:
        x_rotation += X_ROTATE_SPEED
        y_rotation += Y_ROTATE_SPEED
        z_rotation += Z_ROTATE_SPEED
        for i in range(len(CUBE_CORNERS)):
            x = CUBE_CORNERS[i][X]
            y = CUBE_CORNERS[i][Y]
            z = CUBE_CORNERS[i][Z]
            rotated_corners[i] = rotate_point(x, y, z,
                                              x_rotation, y_rotation, z_rotation)

        # Get the points of the cube lines:
        cube_points = []
        for from_corner_index, to_corner_index in ((0, 1), (1, 3), (3, 2), (2, 0),
                                                   (0, 4), (1, 5), (2, 6), (3, 7),
                                                   (4, 5), (5, 7), (7, 6), (6, 4)):
            from_x, from_y = adjust_point(rotated_corners[from_corner_index])
            to_x, to_y = adjust_point(rotated_corners[to_corner_index])
            points_on_line = line(from_x, from_y, to_x, to_y)
            cube_points.extend(points_on_line)

        # Get rid of duplicate points:
        cube_points = tuple(frozenset(cube_points))

        # Display the cube on the screen:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in cube_points:
                    # Display full block:
                    print(LINE_CHAR, end='', flush=False)
                else:
                    # Display empty space:
                    print(' ', end='', flush=False)
            print(flush=False)
        print('Press Ctrl-C to quit.', end='', flush=True)

        time.sleep(PAUSE_AMOUNT)  # Pause for a bit.

        # Clear the screen:
        if sys.platform == 'win32':
            os.system('cls')  # Windows used the cls command.
        else:
            os.system('clear')  # macOS and Linux use the clear command.

except KeyboardInterrupt:
    print('Rotating Cube, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # When Ctrl-C is pressed, end the program.
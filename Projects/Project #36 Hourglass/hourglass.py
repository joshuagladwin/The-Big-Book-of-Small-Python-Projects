"""Hourglass, by Al Sweigart al@inventwithpython.com
An animation of an hourglass with falling sand. Press Ctrl-C to stop.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requries the bext module, which you')
    print('can install by following the instructions at')
    print('https://pyp.org/project/Bext')
    sys.exit()

# Set up the constants:
PAUSE_LENGTH = 0.2  # TODO: Try changing this to 0.0 or 1.0
# TODO: Try changing this to any number between 0 and 100:
WIDE_FALL_CHANCE = 50

SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0  # The index of X values in an (x, y) tuple is 0.
Y = 1  # The index of Y values in an (x, y) tuple is 1.
SAND = chr(9617)
WALL = chr(9608)

# Set up the walls of the hourglass:
HOURGLASS = set()  # Has (x, y) tuples for where hourglass walls are.
# TODO: Try commenting out some HOURGLASS.add() lines to erase walls:
for i in range(18, 37):
    HOURGLASS.add((i, 1))  # Add walls for the top cap of the hourglass.
    HOURGLASS.add((i, 23))  # Add walls for the bottom cap.
for i in range(1, 5):
    HOURGLASS.add((18, i))  # Add walls for the top left straight wall.
    HOURGLASS.add((36, i))  # Add walls for the top right straight wall.
    HOURGLASS.add((18, i + 19))  # Add walls for the bottom left.
    HOURGLASS.add((36, i + 19))  # Add walls for the bottom right.
for i in range(8):
    HOURGLASS.add((19 + i, 5 + i))  # Add the top left slanted wall.
    HOURGLASS.add((35 - i, 5 + i))  # Add the top right slanted wall.
    HOURGLASS.add((25 - i, 13 + i))  # Add the bottom left slanted wall.
    HOURGLASS.add((29 + i, 13 + i))  # Add the bottom right slanted wall.

# Set up the initial sand at the top of the hourglass:
INITIAL_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SAND.add((x, y + 4))


def main():
    bext.fg('yellow')
    bext.clear()

    # Draw the quit message:
    bext.goto(0, 0)
    print('Ctrl-C to quit.', end='')

    # Display the walls of the hourglass:
    for wall in HOURGLASS:
        bext.goto(wall[X], wall[Y])
        print(WALL, end='')

    while True:  # Main program loop.
        all_sand = list(INITIAL_SAND)

        # Draw the initial sand:
        for sand in all_sand:
            bext.goto(sand[X], sand[Y])
            print(SAND, end='')

        run_hourglass_simulation(all_sand)


def run_hourglass_simulation(all_sand):
    """Keep running the sand falling simulation until the sand stops
    moving."""
    while True:  # Keep looping until the sand has run out.
        random.shuffle(all_sand)  # Random order of grain simulation.

        sand_moved_on_this_step = False
        for i, sand in enumerate(all_sand):
            if sand[Y] == SCREEN_HEIGHT - 1:
                # Sand is on the very bottom, so it won't move:
                continue

            # If nothing is under this sand, move it down:
            no_sand_below = (sand[X], sand[Y] + 1) not in all_sand
            no_wall_below = (sand[X], sand[Y] + 1) not in HOURGLASS
            can_fall_down = no_sand_below and no_wall_below

            if can_fall_down:
                # Draw the sand in its new position down one space:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # Clear the old position.
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND, end='')

                # Set the sand in its new position down one space:
                all_sand[i] = (sand[X], sand[Y] + 1)
                sand_moved_on_this_step = True
            else:
                # Check if the sand can fall to the left:
                below_left = (sand[X] - 1, sand[Y] + 1)
                no_sand_below_left = below_left not in all_sand
                no_wall_below_left = below_left not in HOURGLASS
                left = (sand[X] - 1, sand[Y])
                no_wall_left = left not in HOURGLASS
                not_on_left_edge = sand[X] > 0
                can_fall_left = (no_sand_below_left and no_wall_below_left
                                 and no_wall_left and not_on_left_edge)

                # Check if the sand can fall to the right:
                below_right = (sand[X] + 1, sand[Y] + 1)
                no_sand_below_right = below_right not in all_sand
                no_wall_below_right = below_right not in HOURGLASS
                right = (sand[X] + 1, sand[Y])
                no_wall_right = right not in HOURGLASS
                not_on_right_edge = sand[X] < SCREEN_WIDTH - 1
                can_fall_right = (no_sand_below_right and no_wall_below_right
                                  and no_wall_right and not_on_right_edge)

                # Set the falling direction:
                falling_direction = None
                if can_fall_left and not can_fall_right:
                    falling_direction = -1  # Set the sand to fall left.
                elif not can_fall_left and can_fall_right:
                    falling_direction = 1  # Set the sand to fall right.
                elif can_fall_left and can_fall_right:
                    # Both are possible, so randomly set it:
                    falling_direction = random.choice((-1, 1))

                # Check if the sand can "far" fall two spaces to
                # the left or right instead of just one space:
                if random.random() * 100 <= WIDE_FALL_CHANCE:
                    below_two_left = (sand[X] - 2, sand[Y] + 1)
                    no_sand_below_two_left = below_two_left not in all_sand
                    no_wall_below_two_left = below_two_left not in HOURGLASS
                    not_on_second_to_left_edge = sand[X] > 1
                    can_fall_two_left = (can_fall_left and no_sand_below_two_left
                                          and no_wall_below_two_left and not_on_second_to_left_edge)

                    below_two_right = (sand[X] + 2, sand[Y] + 1)
                    no_sand_below_two_right = below_two_right not in all_sand
                    no_wall_below_two_right = below_two_right not in HOURGLASS
                    not_on_second_to_right_edge = sand[X] < SCREEN_WIDTH - 2
                    can_fall_two_right = (can_fall_right
                                          and not_on_second_to_right_edge and no_wall_below_two_right
                                          and not_on_second_to_right_edge)

                    if can_fall_two_left and can_fall_two_right:
                        falling_direction = -2
                    elif not can_fall_two_left and can_fall_two_right:
                        falling_direction = 2
                    elif can_fall_two_left and can_fall_two_right:
                        falling_direction = random.choice((-2, 2))

                if falling_direction == None:
                    # This sand can't fall, so move on.
                    continue

                # Draw the sand in its new position:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')  # Erase old sand.
                bext.goto(sand[X] + falling_direction, sand[Y] + 1)
                print(SAND, end='')  # Draw new sand.

                # Move the grain of sand to its new position:
                all_sand[i] = (sand[X] + falling_direction, sand[Y] + 1)
                sand_moved_on_this_step = True

        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(PAUSE_LENGTH)  # Pause after this

        # If no sand has moved on this step, reset the hourglass:
        if not sand_moved_on_this_step:
            time.sleep(2)
            # Erase all of the sand:
            for sand in all_sand:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
            break  # Break out of main simulation loop.

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

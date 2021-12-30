r"""Rectangles
                                             _____   _____
                               ____   ____  |     | |#####|
                   ___   ___  |    | |####| |     | |#####|
         __   __  |   | |###| |    | |####| |     | |#####|
 _   _  |  | |##| |   | |###| |    | |####| |     | |#####|
|_| |#| |__| |##| |___| |###| |____| |####| |_____| |#####|
"""


def main():
    print('Rectangles')
    # Display rectangle of sizes 0 through 6:
    for rectangle_size in range(0, 6):
        display_outline_rectangle(rectangle_size)
        print()  # Print a newline
        display_filled_rectangle(rectangle_size)
        print()  # Print a newline


def display_outline_rectangle(size):
    # Display the rectangle:
    print(' ', end='')
    print('_' * size)  # Top side of rectangle.
    for i in range(size - 1):
        print('|', end='')  # Left side of rectangle.
        print(' ' * size, end='')  # Interior of rectangle.
        print('|')  # Right side of rectangle.
    # Display the base of the rectangle
    if size > 0:
        print('|', end='')  # Bottom left side of rectangle.
        print('_' * size, end='')  # Bottom side of rectangle.
        print('|')  # Bottom right side of rectangle.


def display_filled_rectangle(size):
    # Display the rectangle:
    print(' ', end='')
    print('_' * size)  # Top side of rectangle.
    for i in range(size - 1):
        print('|', end='')  # Left side of rectangle.
        print('#' * size, end='')  # Interior of rectangle.
        print('|')  # Right side of rectangle.
    # Display the base of the rectangle
    if size > 0:
        print('|', end='')  # Bottom left side of rectangle.
        print('#' * size, end='')  # Bottom side of rectangle.
        print('|')  # Bottom right side of rectangle.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()

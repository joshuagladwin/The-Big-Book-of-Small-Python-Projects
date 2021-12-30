r"""Rhombuses
                                                             ______      ______
                                        _____     _____     /     /     /#####/
                       ____    ____    /    /    /####/    /     /     /#####/
 	      ___   ___   /   /   /###/   /    /    /####/    /     /     /#####/
 __  __  /  /  /##/  /   /   /###/   /    /    /####/    /     /     /#####/
/_/ /#/ /__/  /##/  /___/   /###/   /____/    /####/    /_____/     /#####/
"""


def main():
    print('Rhombuses')
    # Display rhombus of sizes 0 through 6:
    for rhombus_size in range(0, 6):
        display_outline_rhombus(rhombus_size)
        print()  # Print a newline
        display_filled_rhombus(rhombus_size)
        print()  # Print a newline


def display_outline_rhombus(size):
    # Display the rhombus:
    if size > 0:
        print(' ' * size, end='')
        print('_' * (size + 1))  # Top side of rhombus.
        for i in range(size - 1):
            print(' ' * (size - i - 1), end='')
            print('/', end='')  # Left side of rhombus.
            print(' ' * size, end='')  # Interior of rhombus.
            print('/')  # Right side of rhombus.
        # Display the base of the rhombus
        print('/', end='')  # Bottom left side of rhombus.
        print('_' * size, end='')  # Bottom side of rhombus.
        print('/')  # Bottom right side of rhombus.


def display_filled_rhombus(size):
    # Display the rhombus:
    if size > 0:
        print(' ' * size, end='')
        print('_' * (size + 1))  # Top side of rhombus.
        for i in range(size - 1):
            print(' ' * (size - i - 1), end='')
            print('/', end='')  # Left side of rhombus.
            print('#' * size, end='')  # Interior of rhombus.
            print('/')  # Right side of rhombus.
        # Display the base of the rhombus
        print('/', end='')  # Bottom left side of rhombus.
        print('#' * size, end='')  # Bottom side of rhombus.
        print('/')  # Bottom right side of rhombus.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()

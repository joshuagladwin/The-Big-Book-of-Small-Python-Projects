r"""Triangles

                                                    /\         /\
                                 /\       /\       /  \       //\\
                  /\     /\     /  \     //\\     /    \     ///\\\
       /\   /\   /  \   //\\   /    \   ///\\\   /      \   ////\\\\
/\ /\ /__\ //\\ /____\ ///\\\ /______\ ////\\\\ /________\ /////\\\\\
"""


def main():
    print('Triangles')

    # Display triangle of sizes 0 through 6:
    for triangle_size in range(0, 6):
        display_outline_triangle(triangle_size)
        print()  # Print a newline
        display_filled_triangle(triangle_size)
        print()  # Print a newline


def display_outline_triangle(size):
    # Display the triangle:
    for i in range(size-1):
        print(' ' * (size - i - 1), end='')  # Left side space.
        print('/', end='')  # Left side of triangle.
        print(' ' * (i * 2), end='')  # Interior of triangle.
        print('\\')  # Right side of the triangle.
    # Display the base of the triangle
    if size >= 1:
        print('/' + '_' * ((size - 1) * 2) + '\\')  # Base of the triangle.


def display_filled_triangle(size):
    # Display the top half of the triangle:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Left side space.
        print('/' * (i + 1), end='')  # Left side of triangle.
        print('\\' * (i + 1))  # Right side of the triangle.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()

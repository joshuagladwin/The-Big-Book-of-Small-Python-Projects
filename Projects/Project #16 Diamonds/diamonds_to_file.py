r"""Diamonds to File
                                                     /\         /\
                                                    /  \       //\\
                                  /\       /\      /    \     ///\\\
                                 /  \     //\\    /      \   ////\\\\
                   /\     /\    /    \   ///\\\  /        \ /////\\\\\
                  /  \   //\\  /      \ ////\\\\ \        / \\\\\/////
        /\   /\  /    \ ///\\\ \      / \\\\////  \      /   \\\\////
       /  \ //\\ \    / \\\///  \    /   \\\///    \    /     \\\///
/\ /\  \  / \\//  \  /   \\//    \  /     \\//      \  /       \\//
\/ \/   \/   \/    \/     \/      \/       \/        \/         \/
"""


def main():
    print('Diamonds To File')
    d = ''
    # Display diamonds of sizes 0 through 6:
    for diamond_size in range(0, 6):
        s = return_outline_diamond(diamond_size)
        print(s)  # Print a diamond
        d += s + '\n'
        print()  # Print a newline
        f = return_filled_diamond(diamond_size)
        print(f)  # Print a filled diamond
        d += f + '\n'
        print()  # Print a newline

    with open('diamonds.txt', 'w') as f:
        f.write(d)


def return_outline_diamond(size):
    # Display the top half of the diamond:
    s = ''
    for i in range(size):
        s += ' ' * (size - i - 1)  # Left side space.
        s += '/'  # Left side of diamond.
        s += ' ' * (i * 2)  # Interior of diamond.
        s += '\\\n'  # Right side of the diamond.
    # Display the bottom half of the diamond:
    for i in range(size):
        s += ' ' * i  # Left side space.
        s += '\\'  # Left side of diamond.
        s += ' ' * ((size - i - 1) * 2)  # Interior of diamond.
        s += '/\n'  # Right side of diamond.
    return s


def return_filled_diamond(size):
    # Display the top half of the diamond:
    f = ''
    for i in range(size):
        f += ' ' * (size - i - 1)  # Left side space.
        f += '/' * (i + 1)  # Left half of diamond.
        f += '\\' * (i + 1) + '\n'  # Right half of the diamond.
    # Display the bottom half of the diamond:
    for i in range(size):
        f += ' ' * i  # Left side space.
        f += '\\' * (size - i)  # Left side of diamond.
        f += '/' * (size - i) + '\n'  # Right side of the diamond.
    return f


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()

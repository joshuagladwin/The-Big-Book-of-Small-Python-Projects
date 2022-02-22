"""Soroban Japanese Abacus, by Al Sweigart al@inventwithpython.com
A simulation of a Japanese abacus calculator tool.
More info at: https://en.wikipedia.org/wiki/Soroban
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, math, simulation"""

NUMBER_OF_DIGITS = 10


def main():
    print('Soroban - The Japanese Abacus')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    abacus_number = 0  # This is the number represented on the abacus.

    while True:  # Main program loop.
        display_abacus(abacus_number)
        display_controls()

        commands = input('> ').lower()
        if commands == 'quit':
            # Quit the program.
            break
        elif commands.isdecimal():
            # Set the abacus number:
            abacus_number = int(commands)
        else:
            # Handle increment/decrement commands:
            for letter in commands:
                if letter == 'q':
                    abacus_number += 1_000_000_000
                elif letter == 'a':
                    abacus_number -= 1_000_000_000
                elif letter == 'w':
                    abacus_number += 100_000_000
                elif letter == 's':
                    abacus_number -= 100_000_000
                elif letter == 'e':
                    abacus_number += 10_000_000
                elif letter == 'd':
                    abacus_number -= 10_000_000
                elif letter == 'r':
                    abacus_number += 1_000_000
                elif letter == 'f':
                    abacus_number -= 1_000_000
                elif letter == 't':
                    abacus_number += 100_000
                elif letter == 'g':
                    abacus_number -= 100_000
                elif letter == 'y':
                    abacus_number += 10_000
                elif letter == 'h':
                    abacus_number -= 10_000
                elif letter == 'u':
                    abacus_number += 1_000
                elif letter == 'j':
                    abacus_number -= 1_000
                elif letter == 'i':
                    abacus_number += 100
                elif letter == 'k':
                    abacus_number -= 100
                elif letter == 'o':
                    abacus_number += 10
                elif letter == 'l':
                    abacus_number -= 10
                elif letter == 'p':
                    abacus_number += 1
                elif letter == ';':
                    abacus_number -= 1

        # The abacus can't show negative numbers:
        if abacus_number < 0:
            abacus_number = 0  # Change any negative numbers to 0.
        # The abacus can't show numbers larger than 9_999_999_999:
        if abacus_number > 9_999_999_999:
            abacus_number = 9_999_999_999


def display_abacus(number):
    number_list = list(str(number).zfill(NUMBER_OF_DIGITS))

    has_bead = []  # Contains a True of False for each bead position.

    # Top Heaven row has a bead for digits 0, 1, 2, 3, and 4.
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '01234')

    # Bottom Heaven row has a bead for digits 5, 6, 7, 8, and 9.
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '56789')

    # 1st (topmost) earth row has a bead for all digits except 0.
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '123456789')

    # 2nd Earth row has a bead for digits 2, 3, 4, 7, 8 and 9.
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '234789')

    # 3rd Earth row has a bead for digits 0, 3, 4, 5, 8, and 9.
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '034589')

    # 4th Earth row has a bead for digits 0, 1, 2, 4, 5, 6, and 9.
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '0124659')

    # 5th Earth row has a bead for digits 0, 1, 2, 5, 6, and 7.
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '012567')

    # 6th Earth row has a bead for digits 0, 1, 2, 3, 5, 6, 7, and 8.
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '01235678')

    # Convert these True or False values into O or | characters.
    abacus_char = []
    for i, bead_present in enumerate(has_bead):
        if bead_present:
            abacus_char.append('O')
        else:
            abacus_char.append('|')

    # Draw the abacus with the O/| characters.
    chars = abacus_char + number_list
    print("""
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  |  |  |  |  |  |  |  |  |  |  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+""".format(*chars))


def display_controls():
    print('  +q w e r t y u i o p')
    print('  -a s d f g h j k l ;')
    print('(Enter a number, "quit", or a stream of up/down/letters.)')


if __name__ == '__main__':
    main()

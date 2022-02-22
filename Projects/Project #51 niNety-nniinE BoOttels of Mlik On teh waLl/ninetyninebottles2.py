"""niNety-nniinE BoOttels of Mlik On teh waLl
By Al Sweigart al@inventwithpython.com
Print the full lyrics to one of the longest songs ever! The song
gets sillier and sillier with each verse. Press Ctrl-C to stop.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: short, scrolling, word"""

import random, sys, time

# Set up the constants:
# TODO: Try changing both of these to 0 to print all the lyrics at once.
SPEED = 0.1  # The pause in between printing letters.
LINE_PAUSE = 1.5  # The pause at the end of each line.


def slow_print(text, pause_amount=0.1):
    """Slowly print out the characters in text one at a time."""
    for character in text:
        # Set flush=True here so the text is immediately printed:
        print(character, flush=True, end='')  # end='' means no newline.
        time.sleep(pause_amount)  # Pause in between each character.
    print()  # Print a newline.


print('niNety-nniinE BoOttels, by Al Sweigart al@inventwithpython.com')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99  # This is the starting number of bottles.

# This list holds the string used for the lyrics:
lines = [' bottles of milk on the wall,',
         ' bottles of milk,',
         'Take one down, pass it around,',
         ' bottles of milk on the wall!']

try:
    while bottles > 0:  # Keep looping and display the lyrics.
        slow_print(str(bottles) + lines[0], SPEED)
        time.sleep(LINE_PAUSE)
        slow_print(str(bottles) + lines[1], SPEED)
        time.sleep(LINE_PAUSE)
        slow_print(lines[2], SPEED)
        time.sleep(LINE_PAUSE)
        bottles = bottles -1  # Decrease the number of bottles by one.

        if bottles > 0:  # Print the last line of the current stanza.
            slow_print(str(bottles) + lines[3], SPEED)
        else:  # Print the last line of the entire song.
            slow_print('No more bottles of milk on the wall!', SPEED)

        time.sleep(LINE_PAUSE)
        print()  # Print a newline.

        # Choose a random line to make "sillier":
        line_num = random.randint(0, 3)

        # Make a list from the line string so we can edit it. (Strings
        # in Python are immutable.)
        line = list(lines[line_num])

        effect = random.randint(0, 3)
        if effect == 0:  # Replace a character with a space.
            char_index = random.randint(0, len(line) - 1)
            line[char_index] = ' '
        elif effect == 1:  # Change the casing of the character.
            char_index = random.randint(0, len(line) - 1)
            if line[char_index].isupper():
                line[char_index] = line[char_index].lower()
            elif line[char_index].islower():
                line[char_index] = line[char_index].upper()
        elif effect == 2:  # Transpose two characters.
            char_index = random.randint(0, len(line) - 2)
            first_char = line[char_index]
            second_char = line[char_index + 1]
            line[char_index] = second_char
            line[char_index + 1] = first_char
        elif effect == 3:  # Double a character.
            char_index = random.randint(0, len(line) - 2)
            line.insert(char_index, line[char_index])

        # Convert the line list back to a string and put it in lines:
        lines[line_num] = ''.join(line)
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.

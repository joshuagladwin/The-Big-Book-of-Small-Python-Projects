"""Duckling Screensaver, by Al Sweigart al@inventwithpython.com
 A screensaver of many many ducklings.
 
 >" )   =^^)    (``=   ("=  >")    ("=
 (  >)  (  ^)  (v  )  (^ )  ( >)  (v )
  ^ ^    ^ ^    ^ ^    ^^    ^^    ^^
 
 View the original code at https://nostarch.com/big-book-small-python-projects
 Tags: large, artistic, object-oriented, scrolling"""

import random, shutil, sys, time

# Set up the constants:
PAUSE = 0.2  # (!) Try changing this to 1.0 or 0.0.
DENSITY = 0.10  # (!) Try changing this to anything from 0.0 to 1.0.

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1


def main():
    print('Duckling Screensaver, by Al Sweigart')
    print('Press Ctrl-C to quit...')
    time.sleep(2)

    duckling_lanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:  # Main program loop.
        for lane_num, duckling_obj in enumerate(duckling_lanes):
            # See if we should create a duckling in this lane:
            if (duckling_obj == None and random.random() <= DENSITY):
                # Place a duckling in this lane:
                duckling_obj = Duckling()
                duckling_lanes[lane_num] = duckling_obj

            if duckling_obj != None:
                # Draw a duckling if there is one in this lane:
                print(duckling_obj.get_next_body_part(), end='')
                # Delete the duckling if we've finished drawing it:
                if duckling_obj.part_to_display_next == None:
                    duckling_lanes[lane_num] = None
            else:
                # Draw five spaces since there is no duckling here.
                print(' ' * DUCKLING_WIDTH, end='')

        print()  # Print a newline
        sys.stdout.flush()  # Make sure text appears on the screen.
        time.sleep(PAUSE)


class Duckling:
    def __init__(self):
        """Create a new duckling with random body features."""
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            # Chubby ducklings can only have beady eyes.
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        self.part_to_display_next = HEAD

    def get_head_str(self):
        """Returns the string of the duckling's head."""
        head_str = ''
        if self.direction == LEFT:
            # Get the mouth:
            if self.mouth == OPEN:
                head_str += '>'
            elif self.mouth == CLOSED:
                head_str += '='

            # Get the eyes:
            if self.eyes == BEADY and self.body == CHUBBY:
                head_str += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                head_str += '" '
            elif self.eyes == WIDE:
                head_str += "''"
            elif self.eyes == HAPPY:
                head_str += '^^'
            elif self.eyes == ALOOF:
                head_str += '``'

            head_str += ') '  # Get the back of the head.

        if self.direction == RIGHT:
            head_str += ' ('  # Get the back of the head.

            # Get the eyes:
            if self.eyes == BEADY and self.body == CHUBBY:
                head_str += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                head_str += ' "'
            elif self.eyes == WIDE:
                head_str += "''"
            elif self.eyes == HAPPY:
                head_str += '^^'
            elif self.eyes == ALOOF:
                head_str += '``'

            # Get the mouth:
            if self.mouth == OPEN:
                head_str += '<'
            elif self.mouth == CLOSED:
                head_str += '='

        if self.body == CHUBBY:
            # Get an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            head_str += ' '

        return head_str

    def get_body_str(self):
        """Returns the string of the duckling's body."""
        body_str = '('  # Get the left side of the body.
        if self.direction == LEFT:
            # Get the interior body space:
            if self.body == CHUBBY:
                body_str += ' '
            elif self.body == VERY_CHUBBY:
                body_str += '  '

            # Get the wing:
            if self.wing == OUT:
                body_str += '>'
            elif self.wing == UP:
                body_str += '^'
            elif self.wing == DOWN:
                body_str += 'v'

        if self.direction == RIGHT:
            # Get the wing:
            if self.wing == OUT:
                body_str += '<'
            elif self.wing == UP:
                body_str += '^'
            elif self.wing == DOWN:
                body_str += 'v'

            # Get the interior body space:
            if self.body == CHUBBY:
                body_str += ' '
            elif self.body == VERY_CHUBBY:
                body_str += '  '

        body_str += ')'  # Get the right side of the body.

        if self.body == CHUBBY:
            # Get an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            body_str += ' '

        return body_str

    def get_feet_str(self):
        """Returns the string of the duckling's feet."""
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    def get_next_body_part(self):
        """Calls the appropriate display method for the next body
        part that needs to be displayed. Sets part_to_display_next to
        None when finished."""
        if self.part_to_display_next == HEAD:
            self.part_to_display_next = BODY
            return self.get_head_str()
        elif self.part_to_display_next == BODY:
            self.part_to_display_next = FEET
            return self.get_body_str()
        elif self.part_to_display_next == FEET:
            self.part_to_display_next = None
            return self.get_feet_str()


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program

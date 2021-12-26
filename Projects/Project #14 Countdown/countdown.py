"""Countdown, by Al Sweigart al@inventwithpython.com
Show a countdown timer animation using a seven-segment display.
Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
View the original code at httsp://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic"""
import os
import sys, time
import sevseg  # Imports out sevseg.py program.

while True:
    print("Please enter how long to set the timer: (in seconds)")
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        seconds_left = int(response)
        break

    print('Please enter a whole number greater than 0.')
    print()
    continue

try:
    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        os.system('cls')

        # Get the hours/minutes/seconds from seconds_left:
        # For example: 7265 is 2 hours, 1 minute, 5 seconds.
        # So 7265 // 3600 is 2 hours:
        hours = str(seconds_left // 3600)
        # And 7265 % 36000 is 65, and 65 // 60 is 1 minute:
        minutes = str((seconds_left % 3600) // 60)
        # And 7265 % 60 is 5 seconds:
        seconds = str(seconds_left % 60)

        # Get the digit strings from the sevseg module:
        h_digits = sevseg.get_sev_seg_str(hours, 2)
        h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()

        m_digits = sevseg.get_sev_seg_str(minutes, 2)
        m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()

        s_digits = sevseg.get_sev_seg_str(seconds, 2)
        s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

        # Display the digits:
        print(h_top_row     + '     ' + m_top_row       + '     ' + s_top_row)
        print(h_middle_row  + '  *  ' + m_middle_row    + '  *  ' + s_middle_row)
        print(h_bottom_row  + '  *  ' + m_bottom_row    + '  *  ' + s_bottom_row)

        if seconds_left == 0:
            for i in range(0,10):
                os.system('cls')
                time.sleep(0.5)
                print(h_top_row     + '     ' + m_top_row       + '     ' + s_top_row)
                print(h_middle_row  + '  *  ' + m_middle_row    + '  *  ' + s_middle_row)
                print(h_bottom_row  + '  *  ' + m_bottom_row    + '  *  ' + s_bottom_row)
                print()
                print('    * * * * TIME  ELAPSED * * * *    ')
                time.sleep(0.5)
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)  # Insert a one-second pause.
        seconds_left -= 1
except KeyboardInterrupt:
    print('Countdown, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # When Ctrl-C is pressed, end the program.

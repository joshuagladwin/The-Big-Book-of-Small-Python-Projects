"""Bitmap Message, by AL Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, artistic"""

import sys

# TODO: Try using different images.

# There are 68 periods along the top and bottom of this string:
# (You can also copy and past this string from
# https://inventwithpython.com/bitmapworld.txt)
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print("Bitmap Message, by Al Sweigart al@inventwithpython.com")
print("Enter the message to display with the bitmap.")
message = input("> ")
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(" ", end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print()
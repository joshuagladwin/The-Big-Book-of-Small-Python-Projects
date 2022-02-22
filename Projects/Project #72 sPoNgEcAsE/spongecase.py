"""sPoNgEcAsE, by Al Sweigart al@inventwithpython.com
Translates English messages into sPOnGEtExT.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, word"""

import random

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


def main():
    """Run the Spongetext program."""
    print('''sPoNgEcAsE, by aL sWeIgArT Al@iNvEnTwItHpYtHoN.cOm
    
eNtEr YoUr MeSsAge:''')
    spongetext = english_to_spongecase(input('> '))
    print()
    print(spongetext)

    try:
        pyperclip.copy(spongetext)
        print('(cOpIeD SpOnGeTeXt  to ClIpbOaRd)')
    except:
        pass  # Do nothing if pyperclip wasn't installed.


def english_to_spongecase(message):
    """Returns the spongetext form of the given string."""
    spongetext = ''
    use_upper = False

    for character in message:
        if not character.isalpha():
            spongetext += character
            continue

        if use_upper:
            spongetext += character.upper()
        else:
            spongetext += character.lower()

        # Flip the case, 90% of the time.
        if random.randint(1, 100) <= 90:
            use_upper = not use_upper  # Flip the case.
    return spongetext


# If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()

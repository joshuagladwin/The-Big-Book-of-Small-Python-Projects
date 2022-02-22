"""Pig Latin, by Al Sweigart al@inventwithpython.com
Translates English messages into Igpay Atinlay.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: short, word"""

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')


def main():
    print('''Igpay Atinlay (Pig Latin)
By Al Sweigart al@inventwithpython.com

Enter your message:''')
    pig_latin = english_to_pig_latin(input('> '))

    # Join all the words back together into a single string:
    print(pig_latin)

    try:
        pyperclip.copy(pig_latin)
        print('(Copied pg latin to clipboard.)')
    except NameError:
        pass  # Do nothing if pyperclip wasn't installed.


def english_to_pig_latin(message):
    pig_latin = ''  # A string of the pig latin translation.
    for word in message.split():
        # Separate the non-letters at the start of this word:
        prefix_non_letters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]
        if len(word) == 0:
            pig_latin = pig_latin + prefix_non_letters + ' '
            continue

        # Separate the non-letters at the end of this word:
        suffix_non_letters = ''
        while not word[-1].isalpha():
            suffix_non_letters = word[-1] + suffix_non_letters
            word = word[:-1]

        # Remember if the word was in uppercase or titlecase.
        was_upper = word.isupper()
        was_title = word.istitle()

        word = word.lower()  # Make the word lowercase for translation.

        # Separate the consonants at the start of this word:
        prefix_consonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefix_consonants += word[0]
            word = word[1:]

        # Add the pig latin ending to the word:
        if prefix_consonants != '':
            word += prefix_consonants + 'ay'
        else:
            word += 'yay'

        # Set the word back to uppercase or titlecase:
        if was_upper:
            word = word.upper()
        if was_title:
            word = word.title()

        # Add the non-letters back to the start or end of the word.
        pig_latin += prefix_non_letters + word + suffix_non_letters + ' '
    return pig_latin


if __name__ == '__main__':
    main()
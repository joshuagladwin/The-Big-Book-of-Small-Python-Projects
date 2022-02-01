"""Hangman, by Al Sweigart al@inventwithpython.com
Guess the letters to a secret word before the hangman is drawn.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, word, puzzle"""

# A Version of this game is featured in the book "Invent Your Own
# Computer Games with Python" https://nostarch.com/inventwithpython

import random, sys

# Set up the constants:
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

CATEGORY = 'Animals'
WORDS = 'ANT BABOON, BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR' \
        'COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK' \
        'LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT' \
        'PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK' \
        'SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE' \
        'WOLF WOMBAT ZEBRA'.split()

def main():
    print('Hangman, by Al Sweigart al@inventwithpython.com')

    # Setup variables for a new game:
    missed_letters = []  # List of incorrect letter guesses.
    correct_letters = []  # List of correct letter guesses.
    secret_word = random.choice(WORDS)  # The word the player must guess.

    while True:  # Main game loop.
        draw_hangman(missed_letters, correct_letters, secret_word)

        # let the player enter their letter guess:
        guess = get_player_guess(missed_letters + correct_letters)

        if guess in secret_word:
            # Add the correct guess to correct_letters:
            correct_letters.append(guess)

            # Check if the player has won:
            found_all_letters = True  # Start off assuming they've won.
            for secret_word_letter in secret_word:
                if secret_word_letter not in correct_letters:
                    # There's a letter in the secret word that isn't
                    # yet in correct_letters, so the player hasn't won:
                    found_all_letters = False
                    break
            if found_all_letters:
                print(f'Yes! The secret word is: {secret_word}')
                print('You have won!')
                break  # Break out of the main game loop.
        else:
            # The player has guessed incorrectly:
            missed_letters.append(guess)

            # Check if player has guessed too many times and lost. (The
            # "-1" is because we don't count the empty gallows in
            # HANGMAN_PICS.)
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                draw_hangman(missed_letters, correct_letters, secret_word)
                print('You have run out of guesses!')
                print(f'The word was {secret_word}')
                break


def draw_hangman(missed_letters, correct_letters, secret_word):
    """Draw the current state of the hangman, along with the missed and
    correctly-guessed letters of the secret word."""
    print(HANGMAN_PICS[len(missed_letters)])
    print(f'The category is: {CATEGORY}')
    print()

    # Show the incorrectly guessed letters:
    print('Missed letters: ', end='')
    for letter in missed_letters:
        print(letter, end=' ')
    if len(missed_letters) == 0:
        print('No missed letters yet.')
    print()

    # Display the blanks for the secret word (one blank per letter):
    blanks = ['_'] * len(secret_word)

    # Replace the blanks with correctly guessed letters:
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks[i] = secret_word[i]

    # Show the secret word with spaces in between each letter:
    print(' '.join(blanks))


def get_player_guess(already_guessed):
    """Returns the letter the player entered. This function makes sure
    the player entered a single letter they haven't guessed before."""
    while True:  # Keep asking until the player enters a valid letter.
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.ext()  # When Ctrl-C is pressed, end the program.

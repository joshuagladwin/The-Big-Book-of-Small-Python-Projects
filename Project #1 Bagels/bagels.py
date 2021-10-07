"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random


def main():
    print("""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com""")

    # Sets difficulty level.
    num_digits, max_guesses = set_difficulty()

    print(f"""I am thinking of a {num_digits} digit-number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.""")  # TODO: Try to create a version with letters as well as digits.

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess.
        secret_num = get_secret_num(num_digits)
        print("I have thought up a number.")
        print(f"You have {max_guesses} guesses to get it.")

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != num_digits or not guess.isdecimal():
                print(f"Guess #{num_guesses}: ")
                guess = input("> ")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # They're correct so break out of this loop.
            if num_guesses > max_guesses:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}.")

        # Ask the player if they want to play again.  TODO: Allow for changing difficulty at the end of each game.
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith('y'):
            break
    print("Thanks for playing!")


def get_secret_num(num_digits):
    """Returns a string made up of num_digits unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into a random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """Returns a string with the pico, fermi, bagel clues for a guess
    and secret number pair."""
    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


def set_difficulty():
    """Returns num_digits and max_guesses depending on difficulty as set by user."""

    num_digits, max_guesses = 3, 10  # Default values

    difficulty = ''

    while not difficulty.lower().startswith(("e", "m", "h")):
        print("Please select a difficulty level: (easy/medium/hard)")
        difficulty = input("> ")

    if difficulty.lower().startswith('e'):
        num_digits, max_guesses = 2, 5
    elif difficulty.lower().startswith('h'):
        num_digits, max_guesses = 4, 8

    return num_digits, max_guesses


if __name__ == '__main__':
    main()

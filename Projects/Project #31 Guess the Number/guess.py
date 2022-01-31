"""Guess the Number, by Al Sweigart_ al@inventwithpython.com
Try to guess the secret number based on hints.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, game"""

import random


def ask_for_guess():
    while True:
        guess = input('> ')  # Enter the guess.

        if guess.isdecimal():
            return int(guess)  # Convert string guess to an integer.
        print('Please enter a number between 1 and 100.')


print('Guess the Number, by Al Sweigart al@inventwithpython.com')
print()
secret_number = random.randint(1, 100)  # Select a random number.
print('I am thinking of a number between 1 and 100.')

for i in range(10):  # Give the player 10 guesses.
    print(f'You have {10 - i} guesses left. Take a guess.')

    guess = ask_for_guess()
    if guess == secret_number:
        break  # Break out of the for loop if the guess is correct.

    # Offer a hint:
    if guess < secret_number:
        print('Your guess is too low.')
    if guess > secret_number:
        print('Your guess is too high.')

# Reveal the results:
if guess == secret_number:
    print('Yay! You guessed my number!')
else:
    print('Game over. The number I was thinking of was', secret_number)

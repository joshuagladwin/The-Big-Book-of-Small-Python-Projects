"""Hacking Minigame, by Al Sweigart al@inventwithpython.com
The hacking mini-game from "Fallout 3". Find out which seven-letter
word is the password by using clues each guess gives you.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, game, puzzle"""

# NOTE: This program requires the sevenletterwords.txt file. You can
# download it from https://inventwithpython.com/sevenletterwords.txt.

import random, sys

# Set up the constants:
# The garbage filler characters for the "computer memory" display.
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

# Load the WORDS list from a text file that has 7-letter words.
with open('sevenletterwords.txt') as word_list_file:
    WORDS = word_list_file.readlines()
for i in range(len(WORDS)):
    # Convert each word to uppercase and remove the trailing newline:
    WORDS[i] = WORDS[i].strip().upper()


def main():
    """Run a single game of Hacking."""
    print('''Hacking Minigame, by Al Sweigart al@inventwithpython.com
Find the password in the computer's memory. You are given clues after
each guess. For example, if the secret password is MONITOR but the
player guessed CONTAIN, they are given the hint that 2 out of the 7 letters
were correct, because both MONITOR and CONTAIN have the letter O and N
as their 2nd and 3rd letter. You get four guesses.\n''')
    input('Press Enter to begin...')

    game_words = get_words()
    # The "computer memory" is just cosmetic, but it looks cool:
    computer_memory = get_computer_memory_string(game_words)
    secret_password = random.choice(game_words)

    print(computer_memory)
    # Start at 4 tries remaining, going down:
    for tries_remaining in range(4, 0, -1):
        player_move = ask_for_player_guess(game_words, tries_remaining)
        if player_move == secret_password:
            print('A C C E S S   G R A N T E D')
            return
        else:
            num_matches = num_matching_letters(secret_password, player_move)
            print(f'Access Denied ({num_matches}/7 correct)')
    print(f'Out of tries. Secret password was {secret_password}')


def get_words():
    """Return a list of 12 words tha could possibly be the password.

    The secret password will be the first word in the list.
    To make the game fair, we try to ensure that there are words with
    a range of matching numbers of letters as the secret word."""
    secret_password = random.choice(WORDS)
    words = [secret_password]

    # Find two more words; these have zero matching letters.
    # We use "< 3" because the secret passwords is already in words.
    while len(words) < 3:
        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 0:
            words.append(random_word)

    # Find two words that have 3 matching letters (but give up at 500
    # tries if not enough can be found).
    for i in range(500):
        if len(words) == 5:
            break  # Found 5 words, so break out of the loop.

        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 3:
            words.append(random_word)

    # Find at least seven words that have at least one matching letter
    # (but give up at 500 tries if not enough can be found).
    for i in range(500):
        if len(words) == 12:
            break  # Found 7 or more words, so break out of the loop.

        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) != 0:
            words.append(random_word)

    # Add any random words needed to get 12 words total.
    while len(words) < 12:
        random_word = get_one_word_except(words)
        words.append(random_word)

    assert len(words) == 12
    return words


def get_one_word_except(blocklist=None):
    """Returns a random word from WORDS that isn't in blocklist."""
    if blocklist == None:
        blocklist = []

    while True:
        random_word = random.choice(WORDS)
        if random_word not in blocklist:
            return random_word


def num_matching_letters(word1, word2):
    """Returns the number of matching letters in these two words."""
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches


def get_computer_memory_string(words):
    """Return a string representing the "computer memory"."""

    # Pick one line per word to contain a word. There are 16 lines, but
    # they are split into two halves.
    lines_with_words = random.sample(range(16 * 2), len(words))
    # The starting memory address (this is also cosmetic).
    memory_address = 16 * random.randint(0, 4000)

    # Create the "computer memory" string.
    computer_memory = []  # Will contain 16 strings, one for each line.
    next_word = 0  # The index in words of the word to put into a line.
    for line_num in range(16):  # The "computer memory" has 16 lines.
        # Create a half line of garbage characters:
        left_half = ''
        right_half = ''
        for j in range(16):  # Each half line has 16 characters.
            left_half += random.choice(GARBAGE_CHARS)
            right_half += random.choice(GARBAGE_CHARS)

        # Fill in the password from words:
        if line_num in lines_with_words:
            # Find a random place in the half line to insert the word:
            insertion_index = random.randint(0, 9)
            # Insert the word:
            left_half = (left_half[:insertion_index] + words[next_word]
                         + left_half[insertion_index + 7:])
            next_word += 1  # Update the word to put in the half line.
        if line_num + 16 in lines_with_words:
            # Find a random place in the half line to insert the word:
            insertion_index = random.randint(0, 9)
            # Insert the word:
            right_half = (right_half[:insertion_index] + words[next_word]
                          + right_half[insertion_index + 7:])
            next_word += 1  # Update the word to put in the half line.

        computer_memory.append('0x' + hex(memory_address)[2:].zfill(4)
                               + '  ' + left_half + '  '
                               + '0x' + hex(memory_address + (16*16))[2:].zfill(4)
                               + '  ' + right_half)

        memory_address += 16  # Jump from, say, 0xe680 to 0xe690.

    # Each string in the computer_memory list is joing into one large
    # string to return:
    return '\n'.join(computer_memory)


def ask_for_player_guess(words, tries):
    """Let the player enter a password guess."""
    while True:
        print(f'Enter password: ({tries} tries remaining)')
        guess = input('> ').upper()
        if guess in words:
            return guess
        print('That is not one of the possible passwords listed above.')
        print(f'Try entering "{words[0]}" or "{words[1]}".')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

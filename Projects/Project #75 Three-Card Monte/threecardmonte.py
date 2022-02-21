"""Three-Card Monte, by Al Sweigart al@inventwithpython.com
Find the Queen of Hearts after cards have been swapped around.
(In the real-life version, the scammer palms the Queen of Hearts so you
always lose.)
More info at https://en.wikipedia.org/wiki/Three-card_Monte
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, card game, game"""

import random, time

# Set up the constants:
NUM_SWAPS = 16  # TODO: Try changing this to 30 or 100.
DELAY = 0.8  # TODO: Try changing this to 2.0 or 0.0.

# The card suit characters:
HEARTS = chr(9829)  # Character 9829 is '♥'
DIAMONDS = chr(9830)  # Character 9830 is '♦'
SPADES = chr(9824)  # Character 9824 is '♠'
CLUBS = chr(9827)  # Character 9827 is '♣'
# A list of chr() codes is at https://inventwithpython.com/chr

# The indexes of a 3-card list:
LEFT = 0
MIDDLE = 1
RIGHT = 2


def display_cards(cards):
    """Display the cards in "cards", which is a list of (rank, suit)
    tuples."""
    rows = ['', '', '', '', '']  # Stores the text to display.

    for i, card in enumerate(cards):
        rank, suit = card  # The card is a tuple data structure.
        rows[0] += ' ___  '  # Print the top line of the card.
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))


    # Print each row on the screen:
    for i in range(5):
        print(rows[i])


def get_random_card():
    """Returns a random card that is NOT the Queen of Hearts."""
    while True:  # Make cards until you get a non-Queen of Hearts.
        rank = random.choice(list('23456789JQKA') + ['10'])
        suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])

        # Return the card as long as it's not the Queen of Hearts:
        if rank != 'Q' and suit != HEARTS:
            return (rank, suit)


print('Three-Card Monte, by Al Sweigart al@inventwithpython.com')
print()
print('Find the red lady (the Queen of Hearts)! Keep an eye on how')
print('the cards move.')
print()

# Show the original arrangement:
cards = [('Q', HEARTS), get_random_card(), get_random_card()]
random.shuffle(cards)  # Put the Queen of Hearts in a random place.
print('Here are your cards:')
display_cards(cards)
input('Press Enter when you are ready to begin...')

# Print the swaps:
for i in range(NUM_SWAPS):
    swap = random.choice(['l-m', 'm-r', 'l-r', 'm-l', 'r-m', 'r-l'])

    if swap == 'l-m':
        print('swapping left and middle...')
        cards[LEFT], cards[MIDDLE] = cards[MIDDLE], cards[LEFT]
    elif swap == 'm-r':
        print('swapping middle and right...')
        cards[MIDDLE], cards[RIGHT] = cards[RIGHT], cards[MIDDLE]
    elif swap == 'l-r':
        print('swapping left and right...')
        cards[LEFT], cards[RIGHT] = cards[RIGHT], cards[LEFT]
    elif swap == 'm-l':
        print('swapping middle and left...')
        cards[MIDDLE], cards[LEFT] = cards[LEFT], cards[MIDDLE]
    elif swap == 'r-m':
        print('swapping right and middle...')
        cards[RIGHT], cards[MIDDLE] = cards[MIDDLE], cards[RIGHT]
    elif swap == 'r-l':
        print('swapping right and left...')
        cards[RIGHT], cards[LEFT] = cards[LEFT], cards[RIGHT]

    time.sleep(DELAY)

# Print several new lines to hide the swaps.
print('\n' * 60)

# Ask the user to find the red lady:
while True:  # Keep asking until LEFT, MIDDLE, or RIGHT is entered:
    print('Which card has the Queen of Hearts? (LEFT MIDDLE RIGHT)')
    guess = input('> ').upper()

    # Get the index in cards for the position that the player entered:
    if guess in ['LEFT', 'MIDDLE', 'RIGHT']:
        if guess == 'LEFT':
            guess_index = 0
        elif guess == 'MIDDLE':
            guess_index = 1
        elif guess == 'RIGHT':
            guess_index = 2
        break

# TODO: Uncomment this code to make the player always lose:
# if cards[guess_index] == ('Q', HEARTS):
#     # Player has won, so let's move the queen.
#     possible_new_index = [0, 1, 2]
#     possible_new_index.remove(guess_index)  # Remove the queen's index.
#     new_ind = random.choice(possible_new_index)  # Choose a new index.
#     # Place the queen at the new index:
#     cards[guess_index], cards[new_ind] = cards[new_ind], cards[guess_index]

display_cards(cards)  # Show all the cards.

# Check if the player won:
if cards[guess_index] == ('Q', HEARTS):
    print('You won!')
    print('Thanks for playing!')
else:
    print('You lost!')
    print('Thanks for playing!')





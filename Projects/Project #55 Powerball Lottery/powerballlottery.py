"""Powerball Lottery, by Al Sweigart al@inventwithpython.com
A simulation of the lottery so you can experience the thrill of
losing the lottery without wasting your money.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, humor, simulation"""

import random

print('''Powerball Lottery, by Al Sweigart al@inventwithpython.com

Each powerball lottery ticket costs $2. The jackpot for this game
is $1.586 billion! It doesn't matter what the jackpot is, though,
because the odds are 1 in 292,201,338, so you won't win.

This simulation gives you the thrill of playing without wasting money.
''')

# Let the player enter the first five numbers, 1 to 69:
while True:
    print('Enter 5 different number from 1 to 69, with spaces between')
    print('each number. (For example: 5 17 23 42 50)')
    response = input('> ')

    # Check that the player entered 5 things:
    numbers = response.split()
    if len(numbers) != 5:
        print('Please enter 5 numberss, separated by spaces.')
        continue

    # Convert the strings into integers:
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print('Please enter numbers, like 27, 35, or 62.')
        continue

    # Check that the numbers are between 1 and 69:
    for i in range(5):
        if not (1 <= numbers[i] <= 69):
            print('The numbers must all be between 1 and 69.')
            continue

    # Check that the numbers are unique:
    # (Create a set from number to remove duplicates.)
    if len(set(numbers)) != 5:
        print('You must enter 5 different numbers.')
        continue

    break

# Let the player select the powerball, 1 to 26:
while True:
    print('Enter the powerball number from 1 to 26.')
    response = input('> ')

    # Convert the strings into integers:
    try:
        powerball = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22.')
        continue

    # Check that the number is between 1 adn 26:
    if not (1 <= powerball <= 26):
        print('The powerball number be between 1 and 26.')
        continue

    break

# Enter the number of times you want to play:
while True:
    print('How many times do you want to play? (Max: 1000000)')
    response = input('> ')

    # Convert the strings into integers:
    try:
        num_plays = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22000.')
        continue

    # Check that the number is between 1 and 1000000:
    if not (1 <= num_plays <= 1000000):
        print('You can play between 1 and 1000000 times.')
        continue

    break

# Run the simulation:
price = '$' + str(2 * num_plays)
print('It costs', price, 'to play', num_plays, 'times, but don\'t')
print('worry. I\'m sure you\'ll win it all back.')
input('Press Enter to start...')

possible_numbers = list(range(1, 70))
for i in range(num_plays):
    # Come up with lottery numbers:
    random.shuffle(possible_numbers)
    winning_numbers = possible_numbers[0:5]
    winning_powerball = random.randint(1, 26)

    # Display winning numbers:
    print('The winning numbers are: ', end='')
    all_winning_nums = ''
    for i in range(5):
        all_winning_nums += str(winning_numbers[i]) + ' '
    all_winning_nums += 'and ' + str(winning_powerball)
    print(all_winning_nums.ljust(21), end='')

    # NOTE: Sets are not ordered, so it doesn't matter what order the
    # integers in set(numbers) and set(winning_numbers) are.
    if (set(numbers) == set(winning_numbers)
    and powerball == winning_powerball):
        print()
        print('You have won the Powerball Lottery! Congratulations,')
        print('you would be a billionaire if this was real!')
        break
    else:
        print(' You lost.')  # The leading space is required here.

print('You have wasted', price)
print('Thanks for playing!')
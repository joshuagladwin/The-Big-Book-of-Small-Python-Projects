"""Snail Race, by Al Sweigart al@inventwithpython.com
Fast-paced snail racing action!
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, beginner, game, multiplayer"""

import random, time, sys

# Set up the constants:
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40  # TODO: Try modifying this number.

print('''Snail Race, by Al Sweigart al@inventwithpython.com

        @v <-- snail
        
''')

# Ask how many snails to race:
while True:  # Keep asking until the player enters a number.
    print(f'How many snails will race? Max {MAX_NUM_SNAILS}')
    response = input('> ')
    if response.isdecimal():
        num_snails_racing = int(response)
        if 1 < num_snails_racing <= MAX_NUM_SNAILS:
            break
    print(f'Enter a number between 2 and {MAX_NUM_SNAILS}')

# Enter the names of each snail:
snail_names = []  # List of the string snail names.
for i in range(1, num_snails_racing + 1):
    while True:  # Keep asking until the player enters a valid name.
        print(f'Enter snail #{str(i)}\'s name:')
        name = input('> ')
        if len(name) == 0:
            print('Please enter a name')
        elif name in snail_names:
            print('Choose a name that has not already been used.')
        else:
            break  # The entered name is acceptable.
    snail_names.append(name)

# Display each snail at the start line.
print('\n' * 40)
print('START' + (' ' * (FINISH_LINE - len('START'))+ 'FINISH'))
print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
snail_progress = {}
for snail_name in snail_names:
    print(snail_name[:MAX_NAME_LENGTH])
    print('@v')
    snail_progress[snail_name] = 0

time.sleep(1.5)  # The pause right before the race starts.

while True:  # Main program loop.
    # Pick random snails to move forward:
    for i in range(random.randint(1, num_snails_racing // 2)):
        random_snail_name = random.choice(snail_names)
        snail_progress[random_snail_name] += 1

        # Check if a snail has reached the finish line:
        if snail_progress[random_snail_name] == FINISH_LINE:
            print(f'{random_snail_name} has won!')
            sys.exit()

    # TODO: EXPERIMENT: Add a cheat here that increases a snail's progress
    #  if it has your name.

    time.sleep(0.5)  # TODO: EXPERIMENT: Try changing this value.

    # TODO: Experiment: What happens if you comment this line out?
    print('\n' * 40)

    # Display the start and finish lines:
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
    print('|' + (' ' * (FINISH_LINE - 1) + '|'))

    # Display the snails (with name tags):
    for snail_name in snail_names:
        spaces = snail_progress[snail_name]
        print((' ' * spaces) + snail_name[:MAX_NAME_LENGTH])
        print(('.' * snail_progress[snail_name]) + '@v')

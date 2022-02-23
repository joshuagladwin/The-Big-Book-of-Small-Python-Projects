"""Water Bucket Puzzle, by Al Sweigart al@inventwithpython.com
A water pouring puzzle.
More info: https://en.wikipedia.org/wiki/Water_pouring_puzzle
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, math, puzzle"""

import sys


print('Water Bucket Puzzle, by Al Sweigart al@inventwithpython.com')

GOAL = 4  # The exact amount of water to have in a bucket to win.
steps = 0  # Keep trak of how many steps the player made to solve this.

# The amount of water in each bucket:
water_in_bucket = {'8': 0, '5': 0, '3': 0}

while True:  # Main game loop.
    # Display the current state of the buckets:
    print()
    print(f'Try to get {str(GOAL)} L of water into one of these')
    print('buckets:')

    water_display = []  # Contains strings for water or empty space.

    # Get the strings for the 8L bucket:
    for i in range(1, 9):
        if water_in_bucket['8'] < i:
            water_display.append('      ')  # Add empty space.
        else:
            water_display.append('WWWWWW')  # Add water.

    # Get the strings for the 5L bucket.
    for i in range(1, 6):
        if water_in_bucket['5'] < i:
            water_display.append('      ')  # Add empty space.
        else:
            water_display.append('WWWWWW')  # Add water.

    # Get the strings for the 5L bucket.
    for i in range(1, 4):
        if water_in_bucket['3'] < i:
            water_display.append('      ')  # Add empty space.
        else:
            water_display.append('WWWWWW')  # Add water.

    # Display the buckets with the amount of water in each one:
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L
'''.format(*water_display))

    # Check if any of the buckets has the goal amount of water:
    for water_amount in water_in_bucket.values():
        if water_amount == GOAL:
            print(f'Good job! You solved it in {steps} steps!')
            sys.exit()

    # Let the player select an action to do with a bucket:
    print('You can:')
    print('  (F)ill the bucket')
    print('  (E)mpty the bucket')
    print('  (P)our one bucket into another')
    print('  (Q)uit')

    while True:  #Keep asking until the player enters a valid action.
        move = input('> ').upper()
        if move == 'QUIT' or move == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if move in ('F', 'E', 'P'):
            break  # Player has selected a valid action.
        print('Enter F, E, P or Q')

    # Let the player select a bucket:
    while True:  # Keep asking until valid bucket entered.
        print('Select a bucket 8, 5, 3, or QUIT:')
        src_bucket = input('> ').upper()

        if src_bucket == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if src_bucket in ('8', '5', '3',):
            break  # Player has selected a valid bucket.

    # Carry out the selected action:
    if move == 'F':
        # Set the amount of water to the max size.
        src_bucket_size = int(src_bucket)
        water_in_bucket[src_bucket] = src_bucket_size
        steps += 1

    elif move == 'E':
        water_in_bucket[src_bucket] = 0  # Set water amount to nothing.
        steps += 1

    elif move == 'P':
        # Let the player select a bucket to pour into:
        while True:  # Keep asking until valid bucket entered.
            print('Select a bucket to pour into: 8, 5 or 3')
            dst_bucket = input('> ').upper()
            if dst_bucket in ('8', '5', '3',):
                break  # Player has selected a valid bucket.

        # Figure out the amount to pour:
        dst_bucket_size = int(dst_bucket)
        empty_space_in_dst_bucket = dst_bucket_size - water_in_bucket[dst_bucket]
        water_in_src_bucket = water_in_bucket[src_bucket]
        amount_to_pour = min(empty_space_in_dst_bucket, water_in_src_bucket)

        # Pour out water from this bucket:
        water_in_bucket[src_bucket] -= amount_to_pour

        # Put the poured out water into the other bucket:
        water_in_bucket[dst_bucket] += amount_to_pour
        steps += 1

    elif move == 'C':
        pass  # If the player selected Cancel, do nothing.
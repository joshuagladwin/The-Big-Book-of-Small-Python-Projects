"""Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com
A simulation of one million dice rolls.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, math, simulation"""

import random, time
import matplotlib.pyplot as plt

print('''Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com
      
Enter how many six-sided dice you want to roll:''')
number_of_dice = int(input('> '))

# Set up a dictionary to store the results of each dice roll:
results = {}
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    results[i] = 0

# Simulate dice rolls:
print(f'Simulating 1,000,000 rolls of {number_of_dice} dice...')
last_print_time = time.time()
for i in range(1000000):
    if time.time() > last_print_time + 1:
        print(f'{round(i / 10000, 1)}% done...')
        last_print_time = time.time()

    total = 0
    for j in range(number_of_dice):
        total = total + random.randint(1, 6)
    results[total] = results[total] + 1

# Display results:
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print(f'  {i} - {roll} rolls - {percentage}%')

plt.bar(results.keys(), results.values())
plt.title(f'Roll Totals Distribution for 1 Million Rolls of {number_of_dice} Dice')
plt.xlabel('Total')
plt.ylabel('Rolls')
plt.savefig('Curve.png')
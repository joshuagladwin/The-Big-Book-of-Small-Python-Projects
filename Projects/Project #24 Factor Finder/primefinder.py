"""Prime Finder
Finds the first n prime numbers.
"""

import math, sys

print('''Prime Finder

A prime number has only two factors, 1 and the prime number itself.
''')

primes = []


print('Enter a positive whole number (n) to find prime numbers up to the nth prime (or QUIT):')
response = input('> ')
if response.upper() == 'QUIT':
    sys.exit()

if not (response.isdecimal() and int(response) > 0):
    pass
n = int(response)

number = 2

while len(primes) < n:  # Main program loop.

    factors = []

    # Find the factors of number:
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:  # If there's no remainder, it is a factor.
            factors.append(i)
            factors.append(number // i)

    # Convert to a set to get rid of duplicate factors:
    factors = list(set(factors))
    factors.sort()

    if len(factors) == 2:
        primes.append(number)

    number += 1

print(f"The first {n} prime numbers are:")
for p in primes:
    print(p, end=', ')
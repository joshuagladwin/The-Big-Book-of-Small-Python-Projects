"""Numeral System Counters, by Al Sweigart al@inventwithpython.com
Shows equivalent numbers in decimal, hexadecimal, and binary.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, math"""


print('''Numeral System Counters, by Al Sweigart al@inventwithpython.com

This program shows you equivalent numbers in decimal (base 10),
hexadecimal (base 16), and binary (base 2) numeral systems.

(Ctrl-C to quit.)
''')

while True:
    response = input('Enter the starting number (e.g. 0) > ')
    if response == '':
        response = '0'  # Start at 0 by default.
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start = int(response)

while True:
    response = input('Enter how many numbers to display (e.g. 1000) > ')
    if response == '':
        response = '1000'
        break
    if response.isdecimal():
        break
    print('Please enter a number.')
amount = int(response)

for number in range(start, start + amount):  # Main program loop.
    # Convert to hexadecimal/binary and remove the prefix:
    hex_number = hex(number)[2:].upper()
    bin_number = bin(number)[2:]

    print('DEC:', number, '  HEX:', hex_number, '  BIN:', bin_number)
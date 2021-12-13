"""Calendar Maker, by Al Sweigart al@inventwithpython.com
Create monthly calendars, saved to a text file and fit for printing.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short"""

import datetime

# Set up the constants:
DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday')

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print('Calendar Maker, by Al Sweigart al@inventwithpython.com')

while True:  # Loop to get a year from the user.
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2021')
    continue

while True:  # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12:')

while True:  # Loop to get a start day from the user.
    print('Please choose a day of the week to start your week, (MON, TUE, WED, THU, FRI, SAT, SUN')
    response = input('> ')

    if response.upper().startswith('M'):
        start = 0
        break
    elif response.upper().startswith('TU'):
        start = 1
        break
    elif response.upper().startswith('W'):
        start = 2
        break
    elif response.upper().startswith('TH'):
        start = 3
        break
    elif response.upper().startswith('F'):
        start = 4
        break
    elif response.upper().startswith('SA'):
        start = 5
        break
    elif response.upper().startswith('SU'):
        start = 6
        break
    else:
        print('Please choose a day of the week')


def get_calendar_for(year, month, start=0):
    cal_text = ''  # cal_text will contain the string of our calendar.

    # Put the month and year at the top of the calendar:
    cal_text += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Add the days of the week labels to the calendar:
    day_list = []
    day_text = ''
    calendar_padding = '....'

    # Creates the list of abbreviated days:
    for d in DAYS:
        day_list.append(calendar_padding + d[:3].upper() + calendar_padding)

    # Splits the list at the start day, orders the two parts, concats each day to string:
    for d in day_list[start:]:
        day_text += d
    for d in day_list[:start]:
        day_text += d

    cal_text += day_text + '\n'

    # The horizontal line string that separate weeks:
    week_separator = ('+----------' * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separators:
    blank_row = ('|          ' * 7) + '|\n'

    # Get the first date in the month. (The datetime module handles all
    # the complicated calendar stuff for us here.)
    current_date = datetime.date(year, month, 1)

    # Roll back current_date until it's the first instance of the start day. (weekday() returns 0
    # for Monday... 6 for Sunday.)
    while current_date.weekday() != start:
        current_date -= datetime.timedelta(days=1)

    while True:  # Loop over each week in the month.
        cal_text += week_separator

        # day_number_row is the row with the day number labels:
        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += '|' + day_number_label + (' ' * 8)
            current_date += datetime.timedelta(days=1)  # Go to next day.
        day_number_row += '|\n'  # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        cal_text += day_number_row
        for i in range(3):  # (!) Try changing the 4 to a 5 or
            cal_text += blank_row

        # Check if we're done with the month:
        if current_date.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar.
    cal_text += week_separator
    return cal_text


calText = get_calendar_for(year, month, start)
print(calText)  # Display the calendar.

# Save the calendar to a text file:
calendar_filename = f'calendar_{year}_{month}.txt'
with open(calendar_filename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendar_filename)

"""Multiplication Table, by Al Sweigart al@inventwithpython.com
Print a multiplication table.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, math"""

print('Multiplication Table, by Al Sweigart al@inventwithpython.com')

# Print the horizontal number labels:
print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
print('--+---------------------------------------------------')

# Display each row of products:
for number_1 in range(0, 13):

    # Print the vertical numbers label:
    print(str(number_1).rjust(2), end='')

    # Print a separating bar:
    print('|', end='')

    for number_2 in range(0, 13):
        # Print the product followed by a space:
        print(str(number_1 * number_2).rjust(3), end=' ')

    print()  # Finish the row by printing a newline.

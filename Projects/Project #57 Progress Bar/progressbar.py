"""Progress Bar Simulation, by Al Sweigart al@inventwithpython.com
A sample progress bar animation that can be used in other programs.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, module"""

import random, time

BAR = chr(9608)  # Character 9608 is '█'

def main():
    # Simulate a download:
    print('Progress Bar Simulation, by Al Sweigart')
    bytes_downloaded = 0
    download_size = 4096
    while bytes_downloaded < download_size:
        # "Download" a random amount of "bytes":
        bytes_downloaded += random.randint(0, 100)

        # Get the progress bar string for this amount of progress:
        bar_str = get_progress_bar(bytes_downloaded, download_size)

        # Don't print a newline at the end, and immediately flush the
        # printed string to the screen:
        print(bar_str, end='', flush=True)

        time.sleep(0.2)  # Pause for a little bit:

        # Print the backspaces to move the text cursor to the line's start:
        print('\b' * len(bar_str), end='', flush=True)


def get_progress_bar(progress, total, bar_width=40):
    """Returns a string that represents a progress bar that has bar_width
    bars and has progressed progress amount out of a total amount."""

    progress_bar = ''  # The progress bar will be a string value.
    progress_bar += '['  # Create the left end of the progress bar.

    # Make sure that the amount of progress is between 0 and total:
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Calculate the number of "bars" to display:
    number_of_bars = int((progress / total) * bar_width)

    progress_bar += BAR * number_of_bars  # Add the progress bar.
    progress_bar += ' ' * (bar_width - number_of_bars)  # Add empty space.
    progress_bar += ']'  # Add the right end of the progress bar.

    # Calculate the percentage complete:
    percent_complete = round(progress / total * 100, 1)
    progress_bar += ' ' + str(percent_complete) + '%'  # Add percentage.

    # Add the numbers:
    progress_bar += ' ' + str(progress) + '/' + str(total)

    return progress_bar  # Return the progress bar string.


# If the program is run (instead of imported), run main:
if __name__ == '__main__':
    main()

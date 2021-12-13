"""Clickbait Headline Generator, by Al Sweigart al@inventwithpython.com
A clickbait headline generator for your soulless content farm website.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, beginner, humor, word"""

import random

# Set up the constants:
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
COUNTRIES = ['German', 'British', 'Indian', 'Japanese', 'Thai',
          'Algerian', 'Maori', 'Georgian', 'Ethiopian', 'Argentine']
JOBS = ['Athlete', 'Clown', 'Scientist', 'Mathematician', 'Doctor', 'Parent',
       'Dentist', 'Historian', 'Statistician', 'Python Developer', 'Chemist', 'Seismologist',
       'Palaeontologist', 'Serial Killer', 'Geneticist']
THINGS = ['Electron Microscope', 'Machine Learning Model', 'Shovel', 'iPhone', 'Earthquake', 'Parrot',
           'Cat', 'Dog', 'Chicken', 'Robot', 'Gene', 'Chemistry', 'Sushi', 'Diamond', 'Crow',
           'Fossil', 'Gun', 'Pizza', 'Ramen']
PLACES = ['House', 'University', 'Bank Deposit Box', 'School', 'Basement', 'Hospital', 'Mine Shaft',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker', 'Bag', 'Subway Train', 'Mind']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week',
        'In About Half An Hour', 'At Some Point In The Near Future']


def main():
    print('Clickbait Headline Generator')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            number_of_headlines = int(response)
            break  # Exit the loop once a valid number is entered.

    for i in range(number_of_headlines):
        clickbait_type = random.randint(1, 9)

        if clickbait_type == 1:
            headline = generate_are_millennials_killing_headline()
        elif clickbait_type == 2:
            headline = generate_what_you_dont_know_headline()
        elif clickbait_type == 3:
            headline = generate_big_companies_hate_her_headline()
        elif clickbait_type == 4:
            headline = generate_you_wont_believe_headline()
        elif clickbait_type == 5:
            headline = generate_dont_want_you_to_know_headline()
        elif clickbait_type == 6:
            headline = generate_gift_idea_headline()
        elif clickbait_type == 7:
            headline = generate_reasons_why_headline()
        elif clickbait_type == 8:
            headline = generate_job_automated_headline()
        elif clickbait_type == 9:
            headline = generate_which_job_are_you()

        print(headline)
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                             'Facesbook', 'Tweedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print(f'Post these to our {website} {when} or you\'re fired!')


# Each of these functions returns a different type of headline:
def generate_are_millennials_killing_headline():
    thing = random.choice(THINGS)
    return f'Are Millennials Killings the {thing} Industry?'


def generate_what_you_dont_know_headline():
    thing = random.choice(THINGS)
    plural_noun = random.choice(JOBS) + 's'
    when = random.choice(WHEN)
    return f'Without This {thing}, {plural_noun} Could Kill You {when}!'


def generate_big_companies_hate_her_headline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    country = random.choice(COUNTRIES)
    job = random.choice(JOBS)
    thing = random.choice(THINGS)
    return f'Big Companies Hate {pronoun}! See How This {country} {job} Invented a Cheaper {thing}!'


def generate_you_wont_believe_headline():
    country = random.choice(COUNTRIES)
    job = random.choice(JOBS)
    pronoun = random.choice(POSSESSIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f'You Won\'t Believe What This {country} {job} Found in {pronoun} {place}!'


def generate_dont_want_you_to_know_headline():
    plural_job = random.choice(JOBS) + 's'
    plural_thing = random.choice(THINGS) + 's'

    return f'What {plural_job} Don\'t Want You To Know About {plural_thing}'


def generate_gift_idea_headline():
    number = random.randint(7, 15)
    job = random.choice(JOBS)
    country = random.choice(COUNTRIES)
    return f'{number} Gift Ideas to Give Your {country} {job}'


def generate_reasons_why_headline():
    number1 = random.randint(3, 19)
    plural_job = random.choice(JOBS) + 's'
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return f'{number1} Reasons Why {plural_job} Are More Interesting Than You Think ' \
           f'(Number {number2} Will Surprise You!'


def generate_job_automated_headline():
    state = random.choice(COUNTRIES)
    job = random.choice(JOBS)

    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return f'This {state} {job} Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong.'
    else:
        return f'This {state} {job} Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Was Wrong.'


def generate_which_job_are_you():
    country = random.choice(COUNTRIES)
    job = random.choice(JOBS)
    return f'Which Famous {country} {job} are you? Take This Quiz and Find Out!'


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()

"""J'Accuse! by Al Sweigart al@inventwithpython.com
A mystery game of intrigue and a missing cat.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: extra-large, game, humor, puzzle"""

# Play the original Flash game at:
# https://homestarrunner.com/wheresanegg
# More info at: http://www.hrwiki.org/wiki/Where's_an_Egg%3F

import time, random, sys

# Set up the constants:
SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR',
            'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT',
            'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE',
         'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY',
          'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300  # 300 seconds (5 minutes) to solve the game.

# First letters and longest length of places are needed for menu display:
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# Basic sanity checks of the constants:
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
# First letters must be unique:
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)

known_suspects_and_items = []
# visted_places: keys=places, values=strings of the suspect & item there.
visted_places = {}
current_location = 'TAXI'  # Start the game at the taxi.
accused_suspects = []  # Accused suspects won't offer clues.
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusations_left = 3  # You can accuse up to 3 people.
culprit = random.choice(SUSPECTS)

# Common indexes link these; e.g. SUSPECTS[0] and ITEMS[0] are at PLACES[0].
random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

# Create data structures for clues the truth-tellers give about each
# item and suspect.
# clues: key=suspects being asked for a clue, value="clue dictionary".
clues = {}
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue  # Skip the liars for now.

    # This "clue dictionary" has keys=items & suspects,
    # value=the clue given.
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = False  # Useful for debugging.
    for item in ITEMS:  # Select clue about each item.
        if random.randint(0, 1) == 0:  # Tells where the item is:
            clues[interviewee][item] = PLACES[ITEMS.index(item)]
        else:  # Tells who has the item:
            clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]
    for suspect in SUSPECTS:  # Select clue for each suspect.
        if random.randint(0, 1) == 0:  # Tells where the suspect is:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else:  # Tells what item the suspect has:
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]

# Create data structures for clues the liars give about each item
# and suspect:
for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue  # We've already handled the truth-tellers.

    # This "clue dictionary" has keys=items & suspects,
    # value=the clue given:
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = True  # Useful for debugging.

    # This interviewee is a liar and gives wrong clues:
    for item in ITEMS:
        if random.randint(0, 1) == 0:
            while True:  # Select a random (wrong) place clue.
                # Lies about where the item is.
                clues[interviewee][item] = random.choice(PLACES)
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                    # Break out of the loop when wrong clue is selected.
                    break
        else:
            while True:  # Select a random (wrong) suspect clue.
                clues[interviewee][item] = random.choice(SUSPECTS)
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                    # Break out of the loop when wrong clue is selected.
                    break
    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            while True:  # Select a random (wrong) place clue.
                clues[interviewee][suspect] = random.choice(PLACES)
                if clues[interviewee][suspect] != PLACES[ITEMS.index(item)]:
                    # Break out of the loop when wrong clue is selected.
                    break
        else:
            while True:  # Select a random (wrong) item clue.
                clues[interviewee][suspect] = random.choice(ITEMS)
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                    # Break out of the loop when wrong clue is selected.
                    break

# Create the data structures for clues given when asked about Zophie:
zophie_clues = {}
for interviewee in random.sample(SUSPECTS, random.randint(3, 4)):
    kind_of_clue = random.randint(1, 3)
    if kind_of_clue == 1:
        if interviewee not in liars:
            # They tell you who has Zophie.
            zophie_clues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                # Select a (wrong) suspect clue.
                zophie_clues[interviewee] = random.choice(SUSPECTS)
                if zophie_clues[interviewee] != culprit:
                    # Break out of the loop when wrong clue is selected.
                    break
    elif kind_of_clue == 2:
        if interviewee not in liars:
            # They tell you where Zophie is.
            zophie_clues[interviewee] = PLACES[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # Select a (wrong) place clue.
                zophie_clues[interviewee] = random.choice(PLACES)
                if zophie_clues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                    # Break out of the loop when wrong clue is selected.
                    break
    elif kind_of_clue == 3:
        if interviewee not in liars:
            # They tell you what item Zophie is near.
            zophie_clues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # Select a (wrong) item clue.
                zophie_clues[interviewee] = random.choice(ITEMS)
                if zophie_clues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                    # Break out of the loop when wrong clue is selected.
                    break

# EXPERIMENT: Uncomment this code to view the clue data structures:
# import pprint
# pprint.pprint(clues)
# pprint.pprint(zophie_clues)
# print('culprit =', culprit)

# START OF THE GAME
print("""J'ACCUSE! (a mystery game)
By Al Sweigart al@inventwithpython.com
Inspired by Homestar Runner\'s "Where\'s an Egg?" game

You are the world-famous detective Mathilde Camus.
ZOPHIE THE CAT has gone missing, and you must sift through the clues.
Suspects either always tell lies, or always tell the truth. Ask them
about other people, places, and items to see if the details they give are
truthful and consistent with your observations. The you will know if
their clue about ZOPHIE THE CAT is true or not. Will you find ZOPHIE THE
CAT in time and accuse the guilty party?
""")
input('Press Enter to begin...')


start_time = time.time()
end_time = start_time + TIME_TO_SOLVE

while True:  # Main game loop.
    if time.time() > end_time or accusations_left == 0:
        # Handle "game over" condition:
        if time.time() > end_time:
            print('You have run out of time!')
        elif accusations_left == 0:
            print('You have accused too many innocent people!')
        culprit_index = SUSPECTS.index(culprit)
        print(f'It was {culprit} at the {PLACES[culprit_index]} with the {ITEM[culprit_index]} who catnapped her!')
        print('Better luck next time, Detective.')
        sys.exit()

    print()
    minutes_left = int(end_time - time.time()) // 60
    seconds_left = int(end_time - time.time()) % 60
    print(f'Time left: {minutes_left} min, {seconds_left} sec')

    if current_location == 'TAXI':
        print('  You are in your TAXI. Where do you want to go?')
        for place in sorted(PLACES):
            place_info = ''
            if place in visted_places:
                place_info = visted_places[place]
            name_label = '(' + place[0] + ')' + place[1:]
            spacing = " " * (LONGEST_PLACE_NAME_LENGTH - len(place))
            print(f'{name_label} {spacing}{place_info}')
        print('(Q)UIT GAME')
        while True:  # Keep asking until a valid response is given.
            response = input('> ').upper()
            if response == '':
                continue  # Ask again
            if response == 'Q':
                print('Thanks for playing!')
                sys.exit()
            if response in PLACE_FIRST_LETTERS.keys():
                break
        current_location = PLACE_FIRST_LETTERS[response]
        continue  # Go back to the start of the main game loop.

    # At a place; player can ask for clues.
    print(f'  You are at the {current_location}')
    current_location_index = PLACES.index(current_location)
    the_person_here = SUSPECTS[current_location_index]
    the_item_here = ITEMS[current_location_index]
    print(f'  {the_person_here} with the {the_item_here} is here.')

    # Add the suspect and item at this place to our list of known
    # suspects and items:
    if the_person_here not in known_suspects_and_items:
        known_suspects_and_items.append(the_person_here)
    if ITEMS[current_location_index] not in known_suspects_and_items:
        known_suspects_and_items.append(ITEMS[current_location_index])
    if current_location not in visted_places.keys():
        visted_places[current_location] = f'({the_person_here.lower()}, {the_item_here.lower()})'

    # If the player has accused this person wrongly before, they
    # won't give clues:
    if the_person_here in accused_suspects:
        print('They are offended that you accused them,')
        print('and will not help with your investigation.')
        print('You go back to you TAXI.')
        print()
        input('Press Enter to continue...')
        current_location = 'TAXI'
        continue  # Go back to the start of the main game loop.

    # Display menu of known suspects & items to ask about:
    print()
    print(f'(J) "J\'ACCUSE!" ({accusations_left} accusations left)')
    print('(Z) Ask if they know where ZOPHIE THE CAT is.')
    print('(T) Go back to the TAXI.')
    for i, suspect_or_item in enumerate(known_suspects_and_items):
        print(f'({i + 1}) Ask about {suspect_or_item}')

    while True:  # Keep asking until a valid response is given.
        response = input('> ').upper()
        if response in 'JZT' or (response.isdecimal() \
                                 and 0 < int(response) <= len(known_suspects_and_items)):
            break

    if response == 'J':  # Player accuses this suspect.
        accusations_left -= 1  # Use up an accusation.
        if the_person_here == culprit:
            # You've accused the correct suspect.
            print('You\'ve cracked the case, Detective!')
            print(f'It was {culprit} who had catnapped ZOPHIE THE CAT.')
            minutes_taken = int(time.time() - start_time) // 60
            seconds_taken = int(time.time() - start_time) % 60
            print(f'Good job! You solved it in {minutes_taken} min, {seconds_taken} sec.')
            sys.exit()
        else:
            # You've accused the wrong suspect.
            accused_suspects.append(the_person_here)
            print('You have accused the wrong person, Detective!')
            print('They will not help you with anymore clues.')
            print('You go back to your TAXI.')
            current_location = 'TAXI'

    elif response == 'Z':  # Player ask about Zophie.
        if the_person_here not in zophie_clues:
            print('"I don\'t know anything about ZOPHIE THE CAT."')
        elif the_person_here in zophie_clues:
            print(f'  They give you this clue: "{zophie_clues[the_person_here]}"')
            # Add non-place clues to the list of known things:
            if zophie_clues[the_person_here] not in known_suspects_and_items \
                and zophie_clues[the_person_here] not in PLACES:
                known_suspects_and_items.append(zophie_clues[the_person_here])

    elif response == 'T':  # Player goes back to the taxi.
        current_location = 'TAXI'
        continue  # Go back to the start of the main game loop.

    else:  # Player asks about a suspect or item.
        thing_being_asked_about = known_suspects_and_items[int(response) - 1]
        if thing_being_asked_about in (the_person_here, the_item_here):
            print('  They give you this clue: "No comment."')
        else:
            print(f'  They give you this clue:'
                  f' "{clues[the_person_here][thing_being_asked_about]}"')
            # Add non-place clues to the list of known things:
            if clues[the_person_here][thing_being_asked_about] not in known_suspects_and_items \
                and clues[the_person_here][thing_being_asked_about] not in PLACES:
                known_suspects_and_items.append(clues[the_person_here][thing_being_asked_about])

    input('Press Enter to continue...')

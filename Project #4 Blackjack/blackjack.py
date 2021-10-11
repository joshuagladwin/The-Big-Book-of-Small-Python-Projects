"""Blackjack, by Al Sweigart al@inventwithpython.com
The classic card game also known as 21. (This version doesn't have
splitting or insurance.
More info at: https://en.wikipedia.org/wiki/Blackjack
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, card game"""

import random, sys

# Set up the constants:
HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824)  # Character 9824 is '♠'.
CLUBS = chr(9827)  # Character 9827 is '♣'.
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'


def main():
    print("""Blackjack, by Al Sweigart al@inventwithpython.com
    
    Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it is to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    bu must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.""")

    money = 5000
    while True:  # Main game loop.
        # Check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()

        # Let the player enter their bet for this round:
        print("Money:", money)
        bet = get_bet(money)

        # Give the dealer and player two cards from the deck each:
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # Handle player actions:
        print("Bet:", bet)
        while True:  # Keep looping until player stands or busts.
            display_hands(player_hand, dealer_hand, False)
            print()

            # Check if the player has bust:
            if get_hand_value(player_hand) > 21:
                break

            # Get the player's move, either H, S, or D:
            move = get_move(player_hand, money - bet)

            # Handle the player actions:
            if move == 'D':
                # PLayer is doubling down, they can increase their bet:
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f"Bet increased to {bet}.")
                print("Bet:", bet)

            if move in ("H", "D"):
                # Hit/doubling down takes another card.
                new_card = deck.pop()
                rank, suit = new_card
                print(f"You drew a {rank} of {suit}.")
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    # The player has busted:
                    continue

            if move in ("S", "D"):
                # Stand/doubling down stops the player's turn.
                break

        # Handle the dealer's actions:
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                # The dealer hits:
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break  # The dealer has busted.
                input('Press Enter to continue...')
                print("\n\n")

        # Show the final hands:
        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)
        # Handle whether the player won, lost, or tied:
        if dealer_value > 21:
            print(f"Dealer busts! You win €{bet}!")
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print("You lost!")
            money -= bet
        elif player_value > dealer_value:
            print(f'You won €{bet}!')
            money += bet
        elif player_value == dealer_value:
            print("It's a tie, the bet is returned to you.")

        input("Press Enter to continue....")
        print("\n\n")


def get_bet(max_bet):
    """Ask the player how much they want to bet for this round."""
    while True:  # Keep asking until they enter a valid amount.
        print(f"How much do you bet? (1-{max_bet}, or QUIT)")
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue  # If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet  # Player entered a valid bet.


def get_deck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Add the numbered cards.
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))  # Add the face and ace cards.
    random.shuffle(deck)
    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """Show the player's and dealer's cards. Hide the dealer's first
    car if show_dealer_hand is False."""
    print()
    if show_dealer_hand:
        print("DEALER:", get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print("DEALER: ???")
        # Hide the dealer's first card:
        display_cards([BACKSIDE] + dealer_hand[1:])

    # Show the player's cards:
    print("PLAYER:", get_hand_value(player_hand))
    display_cards(player_hand)


def get_hand_value(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are
     worth 11 or 1 (this function picks the most suitable ace value)."""
    value = 0
    number_of_aces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0]  # Card is a tuple like (rank, suit)
        if rank == "A":
            number_of_aces += 1
        elif rank in ("K", "Q", "J"):  # Face cards are worth 10 points.
            value += 10
        else:
            value += int(rank)  # Numbered cards are worth their number.

    # Add the value for the aces:
    value += number_of_aces  # Add 1 per ace.
    for i in range(number_of_aces):
        # If another 10 can be added without busting, do so:
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(cards):
    """Display all the cards in the cards list."""
    rows = ["", "", "", "", ""]  # The text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += " ___  "  # Print the top line of the card.
        if card == BACKSIDE:
            # Print a card's back:
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
        else:
            # Print the card's front:
            rank, suit = card  # The card is a tuple data structure.
            rows[1] += f"|{rank.ljust(2)} | "
            rows[2] += f"| {suit} | "
            rows[3] += f"|_{rank.rjust(2, '_')}| "

    # Print each row on the screen:
    for row in rows:
        print(row)


def get_move(player_hand, money):
    """Asks the player for their move, and returns "H" for hit, "S" for
    stand, and "D" for double down."""
    while True:  # Keep looping until the player enters a correct move.
        # Determine what moves the player can make:
        moves = ["(H)it", "(S)tand"]

        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(player_hand) == 2 and money > 0:
            moves.append("(D)ouble down")

        # Get the player's move:
        move_prompt = ", ".join(moves) + "> "
        move = input(move_prompt).upper()
        if move in ("H", "S"):
            return move  # Player has entered a valid move.
        if move == "D" and "(D)ouble down" in moves:
            return move  # Player has entered a valid move.


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()

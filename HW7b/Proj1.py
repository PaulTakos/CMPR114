# This program uses a dictionary as a deck of cards.
import random

def main():
    # Create a deck of cards.
    deck = create_deck()

    # Get the number of cards to deal.
    # num_cards = int(input('How many cards should I deal? '))

    # Deal the cards.
    deal_cards(deck)

def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades': 11, '2 of Spades': 2, '3 of Spades': 3,
            '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
            '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
            '10 of Spades': 10, 'Jack of Spades': 10,
            'Queen of Spades': 10, 'King of Spades': 10,

            'Ace of Hearts': 11, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
            '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of Clubs': 11, '2 of Clubs': 2, '3 of Clubs': 3,
            '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
            '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
            '10 of Clubs': 10, 'Jack of Clubs': 10,
            'Queen of Clubs': 10, 'King of Clubs': 10,

            'Ace of Diamonds': 11, '2 of Diamonds': 2, '3 of Diamonds': 3,
            '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
            '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
            '10 of Diamonds': 10, 'Jack of Diamonds': 10,
            'Queen of Diamonds': 10, 'King of Diamonds': 10}

    # Returns the deck
    return deck

def deal_cards(deck):
    player1_handvalue = 0
    player2_handvalue = 0

    while len(deck) != 0:
        while player2_handvalue < 21 and player1_handvalue < 21:
            card1 = random.choice(list(deck))
            print('Player 1\'s card: ', card1)
            player1_handvalue += deck[card1]
            if deck[card1] == 11:
                if player1_handvalue > 21:
                    player1_handvalue -= 10
            del deck[card1]

            card2 = random.choice(list(deck))
            print('Player 2\'s card: ', card2)
            player2_handvalue += deck[card2]
            if deck[card2] == 11:
                if player2_handvalue > 21:
                    player2_handvalue -= 10
            del deck[card2]

            print('# of cards left: ', len(deck))
            print('Player 1 score: ', player1_handvalue)
            print('Player 2 score: ', player2_handvalue)

            if len(deck) == 0:
                break

        if player1_handvalue > 21 and player2_handvalue > 21:
            print('No one wins.')
        elif player1_handvalue > 21:
            print('Player 2 wins!')
        elif player2_handvalue > 21:
            print('Player 1 wins!')
        elif player2_handvalue > player1_handvalue:
            print('Player 2 wins!')
        elif player1_handvalue > player2_handvalue:
            print('Player 1 wins!')
        elif player1_handvalue == player2_handvalue:
            print('Tie!')

        if len(deck) == 0:
            print('\nOut of cards, thanks for playing!')

        player1_handvalue = 0
        player2_handvalue = 0

        if len(deck) == 0:
            input('\nType anything to end the game. ')
        else:
            input('\nType anything to start next game.  ')

main()

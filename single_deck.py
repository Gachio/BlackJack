#!/usr/bin/python3

'''
Card Class
'''
# CARD
# SUIT, RANK, VALUE

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

three_of_clubs = Card("Clubs",'Three')
three_of_clubs.value


'''
Deck Class
Objectives of the Deck Class
    Instantiate a new deck
        - Create all 52 Card objects
        - Hold them as a list of Card objects
    Shuffle a Deck through a method call
        - Random library shuffle() function
    Deal cards from the Deck object
        - Pop method from cards list

'''

class Deck:

    def __init__(self):

        self.all_cards = [] # not taking any input from the user

        for suit in suits: # Create essentially all 52 unique cards
            for rank in ranks:
                # Create the card object
                created_card = Card(suit,rank) # creates a new deck

                self.all_cards.append(created_card)

    def shuffle_deck(self): # shuffles the created cards

        random.shuffle(self.all_cards)


    def deal_one(self): # removes a card from all cards
        return self.all_cards.pop()


new_deck = Deck()
new_deck.shuffle_deck()
new_card = new_deck.deal_one()
print(new_card)
last_card = new_deck.all_cards[-1]
print(last_card)


'''
The Player Class

- This class will be used to hold a player's current list of cards.
- A player should be able to add or remove cards from thier "hand" (list of Card Objects).
- I will want the player to be able to add a single card or multiple cards to thier list, so I also explore how to do this in one method call.
- Translate a Deck/Hand of cards with a top and bottom, to a Python list.

* Player Class will have a self.all_cards list
'''

class Player: # creates the Player class

    def __init__(self,name): # distinguishes a player from one another
        self.name = name
        self.all_cards = []

    def remove_one_card(self): # removes a card from list of cards
        return self.all_cards.pop(0)

    def add_cards(self,new_cards): # new_cards can be a single card object of a list of card object
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)

    def __str__(self): # a string method that prints out a player
        return f'Player {self.name} has {len(self.all_cards)} cards.'

new_player = Player("Gachio")
print(new_player)
new_player.add_cards(new_card)
print(new_player)
print(new_player.all_cards[0])


'''
The Game Logic

- Creates two instances of the Player (Player One, Player Two)
- Creates an instance of a new deck, shuffle the deck, and split the deck
'''

# while game_on

round_num = 0 # a counter

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print('Player One is out of Cards! Player Two Wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two is out of cards! Player One Wins!')
        game_on = False
        break

    # START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one_card())

    
    # while at_war
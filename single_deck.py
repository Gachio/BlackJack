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
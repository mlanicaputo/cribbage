from enum import Enum
import random
from typing import List


class Rank(Enum):
    ACE = 1
    R_2 = 2
    R_3 = 3
    R_4 = 4
    R_5 = 5
    R_6 = 6
    R_7 = 7
    R_8 = 8
    R_9 = 9
    R_10 = 10
    JACK = 10
    QUEEN = 10
    KING = 10


class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Card:
    rank: Rank
    suit: Suit

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit


class Deck:
    """
    Cards ordered in face-out order.
    When the deck is face-down on the table, the end of Deck.cards will be
    drawn from. Hence, Deck.draw pops from the end of the list.
    """
    cards: List[Card]

    def __init__(self):
        self.cards = list()

        for suit in Suit:
            for rank in Rank:
                cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self) -> Card:
        # draw a card from the top of the deck
        return self.cards.pop()

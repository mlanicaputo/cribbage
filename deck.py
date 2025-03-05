"""Contains the following classes:
Rank, Suit, Color, Card, Deck.
"""

from enum import Enum
import random
from typing import List


class Rank(Enum):
    """A card rank. E.g. ACE, 2, 9, KING.
    """

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
    JACK = 11
    QUEEN = 12
    KING = 13


class Suit(Enum):
    """A card's suit. E.g. CLUBS, SPADES.
    """

    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3


class Color(Enum):
    """A color. E.g. RED, GREEN.
    """

    BLACK = 0
    RED = 1
    GREEN = 2
    BLUE = 3


class Card:
    rank: Rank
    suit: Suit
    value: int
    color: Color

    def __init__(self, rank: Rank, suit: Suit) -> None:
        self._rank = rank
        self._suit = suit

        self._color = Color.BLACK if suit in (Suit.CLUBS, Suit.SPADES) else Color.RED

        self._value = rank.value if rank.value <= 10 else 10
    

    @property
    def rank(self) -> Rank:
        """Return the card's rank. E.g. Rank.ACE, Rank.R_2.

        Args:
            None
        Returns:
            Rank
        """

        return self._rank

    @property
    def suit(self) -> Suit:
        """Return the card's suit. E.g. Suit.SPADES.

        Args:
            None
        Returns:
            Suit
        """

        return self._suit

    @property
    def value(self) -> int:
        """Return the card's value. E.g. 1, 4, 10.

        Args:
            None
        Returns:
            Rank
        """

        return self._value

    @property
    def color(self) -> Color:
        """Return the card's color. E.g. Color.RED.

        Args:
            None
        Returns:
            Color
        """

        return self._color


class Deck:
    """
    Cards ordered in face-out order.
    When the deck is face-down on the table, the end of Deck.cards will be
    drawn from. Hence, Deck.draw pops from the end of the list.
    """
    cards: List[Card]

    def __init__(self, shuffle=True) -> None:
        self._cards = list()

        for suit in Suit:
            for rank in Rank:
                self._cards.append(Card(rank, suit))

        if shuffle:
            self.shuffle()

    @property
    def cards(self):
        """Return cards in the deck.
        """

        return self._cards

    def shuffle(self) -> None:
        """Shuffle the deck, reordering cards randomly.
        """

        random.shuffle(self.cards)

    def draw(self) -> Card:
        """Draw a card from the top of the deck.
        """

        return self.cards.pop()

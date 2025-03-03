from deck import *
from typing import List


class Hand:
    """
    The cards a player has in their hand.
    """
    cards: List[Card]

    def __init__(self):
        cards = list()

    def add_card(self, card) -> None:
        """
        Add a card to the hand.
        """
        # should this accept a list OR a single card?
        # catch exception when adding too many cards to a hand??
        self.cards.append(card)

    def remove_card(self, card) -> Card:
        """
        Remove and return a card from the hand.
        """
        # catch exception when removing cards from an empty hand??
        removed_card = self.cards.remove(card)
        return removed_card


    def clear(self) -> None:
        """
        Empty the hand of cards. Dereferences current hand's cards field.
        """
        # catch exception when hand is empty? or allow to clear empty hands?
        self.cards = list()

    def get_value(self) -> int:
        """
        Get the value of the hand.
        Return the number of points in the hand.
        """
        pass


class HandSpace(Hand):
    """
    The space where a player's visible cards lie.
    """


class Player:
    """
    A player.
    """
    is_dealer: bool
    hand: Hand
    handspace: HandSpace
    crib: Hand
    cribspace: HandSpace


class Peg:
    """
    A peg.
    """
    # TODO color
    value: int


class Track:
    """
    A track for pegs on the board.
    """
    length: int
    pegs: List[Peg]
    player: Player
    # TODO color


class Board:
    """
    A board.
    """
    track1: Track
    track2: Track
    track3: Track
    win_track: Track

from deck import *

class TestRank:
    def test_rank(self):
        ace = Rank(1)
        assert ace == Rank.ACE

        two = Rank(2)
        assert two == Rank.R_2

        jack = Rank(11)
        assert jack == Rank.JACK

        queen = Rank(12)
        assert queen == Rank.QUEEN

        assert jack != queen


class TestSuit:
    def test_suit(self):
        clubs = Suit(0)
        assert clubs == Suit.CLUBS

        diamonds = Suit(1)
        assert diamonds == Suit.DIAMONDS

        assert clubs != diamonds


class TestColor:
    def test_color(self):
        black = Color(0)
        assert black == Color.BLACK

        red = Color(1)
        assert red == Color.RED

        assert red != black



class TestCard:
    def test_card(self):
        ace_of_clubs = Card(Rank.ACE, Suit.CLUBS)
        assert ace_of_clubs.rank == Rank.ACE
        assert ace_of_clubs.suit == Suit.CLUBS
        assert ace_of_clubs.value == 1
        assert ace_of_clubs.color == Color.BLACK

        ten_of_hearts = Card(Rank.R_10, Suit.HEARTS)
        assert ten_of_hearts.rank == Rank.R_10
        assert ten_of_hearts.suit == Suit.HEARTS
        assert ten_of_hearts.value == 10
        assert ten_of_hearts.color == Color.RED

        jack_of_diamonds = Card(Rank.JACK, Suit.DIAMONDS)
        assert jack_of_diamonds.rank == Rank.JACK
        assert jack_of_diamonds.suit == Suit.DIAMONDS
        assert jack_of_diamonds.value == 10
        assert jack_of_diamonds.color == Color.RED

        assert ten_of_hearts.value == jack_of_diamonds.value
        assert ten_of_hearts.rank.value != jack_of_diamonds.rank.value


class TestDeck:
    def test_deck(self):
        deck = Deck()
        assert len(deck.cards) == 52

        drawn_card = deck.draw()
        assert type(drawn_card) == Card
        assert len(deck.cards) == 51

        # TODO How to test shuffle? It is technically possible to get the same
        # output as input with the random.shuffle(). Therefore, we cannot test
        # whether the list was reordered or not--the test would fail a non-zero
        # percent of the time.

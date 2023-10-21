import pytest
from twentyone import Dealer, _next_card, _hand_total


@pytest.fixture
def dealer():
    return Dealer()


def test_new_round(dealer):
    dealer.new_round()
    assert len(dealer.hand) == 2


def test_get_hand_total():
    hand = ['A', 'K']
    total = _hand_total(hand)
    assert total == 21


def test_determine_play():
    dealer = Dealer()
    assert dealer.determine_play(16) == 'hit'
    assert dealer.determine_play(17) == 'stand'


def test_make_play():
    dealer = Dealer()
    dealer.new_round()
    play = dealer.make_play()
    assert play in ['hit', 'stand']

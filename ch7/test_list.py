"""
Test Cases
* `list` from an empty database
* `list` from a non-empty database
"""
from cards import Card
import pytest


def test_list_no_cards(cards_db):
    """Empty db, empty list"""
    assert cards_db.list_cards() == []

def test_list_several_cards(cards_db):
    """
    Given a variety of cards, make sure they get returned.
    """
    orig = [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]

    for c in orig:
        cards_db.add_card(c)

    the_list = cards_db.list_cards()

    assert len(the_list) == len(orig)
    for c in orig:
        assert c in the_list

@pytest.fixture(scope="function")
def cards_db_cards_owner_state(cards_db):
    """CardsDB with 3 cards with owners and states"""
    cards_db.add_card(Card("foo"))
    cards_db.add_card(Card("bar", owner="me"))
    cards_db.add_card(Card("baz", owner="you", state="in prog"))
    cards_db.add_card(Card("baz", owner="me", state="in prog"))
    return cards_db

def test_filter_owner(cards_db_cards_owner_state):
    result = cards_db_cards_owner_state.list_cards(owner="me")

    assert len(result) == 2
    assert result[0].owner == "me"

def test_filter_state(cards_db_cards_owner_state):
    result = cards_db_cards_owner_state.list_cards(state="in prog")

    assert len(result) == 2
    assert result[0].state == "in prog"

def test_filter_owner_state(cards_db_cards_owner_state):
    result = cards_db_cards_owner_state.list_cards(owner="me", state="in prog")

    assert len(result) == 1
    assert result[0].owner == "me"
    assert result[0].state == "in prog"
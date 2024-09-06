import pytest
from cards import Card

# Three test functions that ensure any start state results "in prog" when start is called
def test_start_from_done(cards_db):
    """Test that starting a card from 'done' results in 'in prog'"""
    c = Card("write a book", state="done")
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

def test_start_from_in_prog(cards_db):
    """Test that starting a card from 'in prog' results in 'in prog'"""
    c = Card("write a book", state="in prog")
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

def test_start_from_todo(cards_db):
    """Test that starting a card from 'todo' results in 'in prog'"""
    c = Card("write a book", state="todo")
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

# Function that uses function parameterization to test all three start states
@pytest.mark.parametrize("start_state", ["done", "in prog", "todo"])
def test_start(cards_db, start_state):
    """Test that starting a card from any state results in 'in prog'"""
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

# Function that uses fixture parameterization to test all three finish states
@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param

def test_start_fix_param(cards_db, start_state):
    """Test that starting a card from any state results in 'in prog'"""
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

# Function that uses pytest_generate_tests to test all three finish states
def pytest_generate_tests(metafunc):
    if "start_state2" in metafunc.fixturenames:
        metafunc.parametrize("start_state2", ["done", "in prog", "todo"])

def test_start_gen_tests(cards_db, start_state2):
    """Test that starting a card from any state results in 'in prog'"""
    c = Card("write a book", state=start_state2)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"
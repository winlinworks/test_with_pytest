"""Demonstrate simple fixtures."""

import pytest


@pytest.fixture(scope="module")
def some_data():
    """Return answer to ultimate question."""
    return 42

def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42

def test_some_data_again(some_data):
    """Demonstrate that fixtures are run before tests."""
    with pytest.raises(AssertionError):
        assert some_data == 41


@pytest.fixture(scope="module")
def some_other_data():
    """Return dictionary of test values."""
    print("Setup some_other_data fixture")
    yield {"a": 1, "b": 2, "c": 3}
    print("Teardown some_other_data fixture")

def test_some_other_data(some_other_data):
    """Check value of a."""
    assert some_other_data['a'] == 1

def test_other_data(some_other_data):
    """Check value of b"""
    assert some_other_data['b'] == 2


@pytest.fixture()
def a_tuple():
    """Return something more interesting."""
    return (1, "foo", None, {"bar": 32})


def test_a_tuple(a_tuple):
    """Demo the a_tuple fixture."""
    assert a_tuple[3]["bar"] == 32



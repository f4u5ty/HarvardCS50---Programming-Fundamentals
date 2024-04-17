import pytest
from bank import value

def test_hwords():
    assert value("how are you?") == 20
    assert value("heller?") == 20
    assert value("hi how are ya?") == 20

def test_hello():
    assert value("hello there") == 0
    assert value("Hello there") == 0

def test_other():
    assert value("you dirty slut") == 100
    assert value("Likahimowa") == 100

#seems like they want us to on purpose, mess the program up.


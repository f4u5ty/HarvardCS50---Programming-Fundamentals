import pytest
from fuel import convert, gauge


def test_valid_fraction():
    assert convert("3/4") == 75

def test_invalid_fraction():
    with pytest.raises(ValueError):
        convert("elshaddai/2")

def test_ZeroDivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_ValueError():
    with pytest.raises(ValueError):
        convert("cat/1")

#these are all convert tests.

def test_99percent():
    assert gauge(99) == "F"

def test_100percent():
    assert gauge(100) == "F"

def test_1percent():
    assert gauge(1) == "E"

def test_correct_percent():
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"










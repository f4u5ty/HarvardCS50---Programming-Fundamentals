import pytest
from twttr import shorten


def test_shorten():
    assert shorten("CS50P") == "CS50P"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("Python is snake language") == "Pythn s snk lngg"
    assert shorten("Twitter") == "Twttr"

def test_consonants():
    assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"
    assert shorten("87") == "87"

def test_vowels():
    assert shorten("aeiou") == ""

def test_numbers():
    assert shorten("0123456789") == "0123456789"

def test_capitalization():
    assert shorten("AEIOUX") == "X"









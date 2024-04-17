import pytest
from plates import is_valid




def test_alphabetical():
    assert is_valid("50CS") == False
    assert is_valid("A") == False
    assert is_valid("BB") == True
    assert is_valid("B1") == False
    assert is_valid("6") == False

def test_length():
    assert is_valid("CSPP50") == True
    assert is_valid("CSPP878") == False
    assert is_valid("") == False

def test_numbers_betwixt():
    assert is_valid("CS50P") == False
    assert is_valid("ME87P") == False
    assert is_valid("3030") == False
    assert is_valid("LE87") == True

def test_special_chars():
    assert is_valid("CS50@") == False
    assert is_valid("ME87#$") == False

def test_zero():
    assert is_valid("00") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_beginning():
    assert is_valid("ELSHAD") == True
    assert is_valid("ELOHIM") == True
    assert is_valid("11") == False




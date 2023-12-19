from numb3rs import validate
import sys

def main():
    test_format()
    test_nums()

def test_format():
    assert validate(r"127.0.0.1") == True
    assert validate(r"127.0.0") == False
    assert validate(r"127.0") == False
    assert validate(r"127") == False
def test_word():
    assert validate(r"Cat") == False

def test_nums():
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.1.1.1") == False
    assert validate(r"1.512.1.1") == False
    assert validate(r"1.1.512.1") == False
    assert validate(r"1.1.1.512") == False

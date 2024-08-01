from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("Cat/Dog")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"

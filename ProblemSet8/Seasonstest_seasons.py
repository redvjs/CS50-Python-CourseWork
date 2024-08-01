from seasons import converter
import pytest
import sys

def main():
    test_date()

def test_date():
    assert converter("2021-12-23") == "Five hundred twenty-five thousand, six hundred minutes"
    with pytest.raises(SystemExit) as excinfo:
        converter("January, 1st 2020")
        converter("1996.10.29")
    assert excinfo.value.code == "Invalid date"



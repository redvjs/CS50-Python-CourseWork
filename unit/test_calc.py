from unit import square

def test_pos():
    assert square(2) == 4
    assert square(3) == 9
def test_neg():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0

# now run pytest test_calc.py
# this will test the program for you

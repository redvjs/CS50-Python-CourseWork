from bank import value
def main():
    test_returns()
    test_upper_lower()


def test_returns():
    assert value("hello") == 0
    assert value("house") == 20
    assert value("zinc") == 100

def test_upper_lower():
    assert value("HeLLO") == 0
    assert value("HaeMatOlogY") == 20
    assert value("ZiNc") == 100



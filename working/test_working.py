from working import convert

def main():
    test_conversions()


def test_conversions():
    assert convert("6:30 AM to 6:30 PM") == "06:30 to 18:30"
    assert convert("6:30 PM to 6:30 AM") == "18:30 to 06:30"
    assert convert("6:30 AM to 6:30 AM") == "06:30 to 06:30"
    assert convert("6:30 PM to 6:30 PM") == "18:30 to 18:30"
def test_wrong_input():
    assert convert("6 to 6") == "None"
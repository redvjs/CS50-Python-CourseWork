from twttr import shorten
def main():
    test_shorten()
    test_lower()
    test_cases()
    test_non_alpha()
    test_punctuation()

def test_shorten():
    assert shorten("twitter") == "twttr"

def test_lower():
    assert shorten("TWITTER") == "TWTTR"

def test_cases():
    assert shorten("TwITtEr") == "TwTtr"

def test_non_alpha():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("!?.,") == "!?.,"


if __name__ == "__main__":
    main()
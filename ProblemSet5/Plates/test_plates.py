from plates import is_valid

def main():
    test_length()

def test_length():
    assert is_valid("aaaaaa") == True
    assert is_valid("aaaaaaa") == False
    assert is_valid("aa") == True
    assert is_valid("a") == False
def test_startswith():
    assert is_valid("aa1") == True
    assert is_valid("a1a") == False
    assert is_valid("1aa") == False
    assert is_valid("a11") == False
def test_not0():
    assert is_valid("aaa110") == True
    assert is_valid("aaa010") == False
def test_endswith():
    assert is_valid("aaa111") == True
    assert is_valid("aaa11a") == False
    assert is_valid("aaaaa1") == True
    assert is_valid("aa1aa1") == False
def test_alphanum():
    assert is_valid("11aa") == False
    assert is_valid("a1aa") == False
    assert is_valid("aa11") == True
    assert is_valid("1a") == False
    assert is_valid("a1") == False
    assert is_valid("11") == False
def test_specialchar():
    assert is_valid("!!") == False
    assert is_valid(".!") == False
    assert is_valid("@*") == False
    assert is_valid("aa!") == False
    assert is_valid("!aa!") == False
    assert is_valid("aa!1") == False
    assert is_valid("aaa!2!") == False

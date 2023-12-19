def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif len(s) >= 4 and s[3:].isnumeric() and s[3:].startswith("0"):
        return False
    elif s.isalpha():
        return True
    elif s[2].isnumeric() and s[3:].isalnum():
        return False
    elif s.isalnum() and len(s) == 3 and s[:2].isalpha() and s[1:].isnumeric() and s[2] != "0":
        return True
    elif s[:2].isalpha() and s.isalnum() and s[-1].isnumeric() and s[-2:][0] != "0":
        return True
    else:
        return False


if __name__ == "__main__":
    main()
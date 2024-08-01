def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif s.isalpha():
        return True
    elif s[0:2].isalpha() and s.isalnum() and s[-2].isnumeric() and s[-2:][0] != "0":
        return True
    else:
        return False

main()

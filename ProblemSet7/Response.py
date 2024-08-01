from validator_collection import validators, checkers, errors

def main():
    ask = validate(input("What's your email address?: "))
def validate(s):
    try:
        if check := checkers.is_email(s) == True:
            print("Valid")
        else:
            print("Invalid")
    except errors.InvalidEmailError as error:
        print("Invalid")

if __name__ == "__main__":
    main()

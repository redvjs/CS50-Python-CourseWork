def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("x should be a number")
# can also use "pass" in order to simply pass over the except ValueError
# except ValueError:
#    pass
main()
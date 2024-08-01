import random


def main():
    level = get_level()
    score = game(level)
    print("Score: ", score)


def get_level():
    while True:
        try:
            allowed = [1, 2, 3]
            level = int(input("Level: "))
            if level in allowed:
                break
        except ValueError:
            pass
    return level
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x, y

def round(x,y):
    mistakes = 1
    while mistakes <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                mistakes += 1
                print("EEE")
        except ValueError:
            mistakes += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False

def game(level):
    rounds = 1
    score = 0
    while rounds <= 10:
        x, y = generate_integer(level)
        ans = round(x,y)
        if ans == True:
            score += 1
        rounds += 1
    return score

if __name__ == "__main__":
    main()

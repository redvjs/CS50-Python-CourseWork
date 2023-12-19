import random

while True:
    try:
        level = int(input("Level: "))
        if level < 0:
            print("Must be Positive")
        else:
            break
    except (EOFError, ValueError):
         print("Must be an integer")
while True:
    try:
        guess = int(input("Guess: "))
        rand = random.randint(1, level)
        if guess > rand:
            print("Too large!")
        elif guess < rand:
            print("Too small!")
        else:
            print("Just right!")
            break

    except (EOFError, ValueError):
        print("Must be an integer")

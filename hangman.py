import random

def play_hangman():
    word_list = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape", "huckleberry"]
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left")
        print("Used letters:", ' '.join(used_letters))
        print("Word:", " ".join([letter if letter in used_letters else '_' for letter in word]))

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet:
            if user_letter in used_letters:
                print("You have already used that letter")
            elif user_letter in word_letters:
                print("That letter is in the word!")
                word_letters.remove(user_letter)
            else:
                print("That letter is not in the word")
                lives -= 1
            used_letters.add(user_letter)
        else:
            print("Invalid input, please try again")

    if len(word_letters) == 0:
        print("Congratulations! You won!")
    else:
        print("You lost :( The word was", word)

play_hangman()

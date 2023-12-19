def main():
    user_input = shorten(input("Input: "))
    input_stripped = shorten(user_input)
    print(f"Output: {input_stripped}")

def shorten(word):
    input_stripped = ""
    for non_vowel in word:
        if not non_vowel.lower() in ["a","o","u","i","e"]:
            input_stripped += non_vowel
    return input_stripped

if __name__ == "__main__":
    main()




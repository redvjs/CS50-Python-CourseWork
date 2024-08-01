type = input("Input: ")
print("Output: ", end="")
for vowel in type:
    if not vowel.lower() in ["a", "u", "i", "o", "e"]:
        print(vowel, end="")
print()


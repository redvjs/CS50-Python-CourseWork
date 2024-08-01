def main():
   message = convert(input("Are you :) or :(? "))


def convert(c):
    message_seperate = c.split(" ")
    convert = ""
    for word in message_seperate:
       convert += emojis.get(word, word) + " "
    print(convert)


emojis = {
        ":)": "🙂",
        ":(": "🙁",
        ":),": "🙂,",
        ":).": "🙂.",
        ":(,": "🙁,",
        ":(.": "🙁."
}
main()

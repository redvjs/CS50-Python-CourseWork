from pyfiglet import Figlet
import sys
import random
figlet = Figlet()


user_args = sys.argv[1:]

if len(user_args) == 1:
    sys.exit("Too few arguments")
elif len(user_args) == 3:
    sys.exit("Too many arguments")
elif not str(sys.argv[1]).startswith("-f") and not str(sys.argv[1]).startswith("--font"):
    sys.exit("Wrong input")
elif sys.argv[2] not in figlet.getFonts():
    sys.exit(1)
else:
    pass

input = input("Input: ")

fonts = figlet.getFonts()

try:
    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(input))
except:
    print("Invalid font")
    sys.exit


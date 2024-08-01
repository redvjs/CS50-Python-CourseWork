import inflect
import sys

list = []
p = inflect.engine()
while True:
    try:
        name = input()
        list.append(name)
    except EOFError:
        print()
        break
joined = p.join((list))
print("Adieu, adieu, to", joined)


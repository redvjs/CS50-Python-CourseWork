list = {}

sortedlist = dict(sorted(list.items(), key=lambda x:x.upper()))

while True:
    try:
        item = input().upper()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1

    except (EOFError, KeyError):
        sortedlist = dict(sorted(list.items(), key=lambda x:x))
        for key, value in sortedlist.items():
            print(value, key)
        break